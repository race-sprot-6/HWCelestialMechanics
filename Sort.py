import numpy as np
#import scipy
#import numpy as np
import math as m
import matplotlib.pyplot as plt
import scipy.interpolate
#координаты САО в градусах
la = 0.72344
fi = 0.76475
al = 4.92576
de = 0.01047
Nh = 3
ko = 1.002738
S0 = 1
file = open("Uraw.dat", "r")
file_with_lines = file.readlines()[0:132]

all = []
Umagn = []
Time = []

for line in file_with_lines:
    a = line.split(" ")
    a = [x.strip('\n') for x in a]
    all.append(a)
StEl = []
for i in range(0, int(len(all)/2)):
    StEl.append(all[2*i]+all[2*i+1])
for i in range(0, len(StEl)):
    if StEl[i][0] == '-':
        StEl[i][0] = StEl[i-1][0]
name = []
for i in range(1, len(StEl)):
    N = StEl[i][0]
    name.append(N)
from collections import OrderedDict #убираем дубли, трибли, и тд
Name = list(OrderedDict.fromkeys(name))
FonT = []
FonB = []
CompT = []
CompB = []

j = 0
prT1 = []
prT2 = []
prB1 = []
prB2 = []
for i in range(3, len(StEl)):

    if StEl[i][0] == Name[1]:
        prT1.append(StEl[i][1])
        prB1.append(StEl[i][4])
    else:
        if StEl[i][0] != Name[1] and prB1 != []:
            FonT.append(prT1)
            FonB.append(prB1)
            prT1 = []
            prB1 = []


    if StEl[i][0] == Name[2]:
        prT2.append(StEl[i][1])
        prB2.append(StEl[i][4])
    else:
        if StEl[i][0] != Name[2] and prT2 != []:
            CompT.append(prT2)
            CompB.append(prB2)
            prT2 = []
            prB2 = []
#FonT = [x.strip([]) for x in FonT]
#for ele in FonB:
    #if ele == "[]":
        #FonB.remove(ele)
SrFonB = []
sumB = 0
for i in range(0, len(FonB)):
    for k in range(0, len(FonB[i])):
        sumB = sumB + int(FonB[i][k])
    sredB = sumB/(len(FonB[i]))/10
    SrFonB.append(sredB)
    sumB = 0
SrCompB = [] #список со средними компами
sumB = 0
for i in range(0, len(CompB)):
    for k in range(0, len(CompB[i])):
        sumB = sumB + int(CompB[i][k])
    sredB = sumB/(len(CompB[i]))/10
    SrCompB.append(sredB)
    sumB = 0
SrFonT = []
for i in range(0, len(FonT)):
    for k in range(0, len(FonT[i])):
        t = int(FonT[i][k][0:2]) + int(FonT[i][k][3:5])/60 + int(FonT[i][k][6:8])/3600
        FonT[i][k] = t
    sr = (FonT[i][0] + FonT[i][-1])/2
    SrFonT.append(sr)
SrCompT = []
for i in range(0, len(CompT)):
    for k in range(0, len(CompT[i])):
        t = int(CompT[i][k][0:2]) + int(CompT[i][k][3:5])/60 + int(CompT[i][k][6:8])/3600
        CompT[i][k] = t
    sr = (CompT[i][0] + CompT[i][-1])/2
    SrCompT.append(sr)
new_file = open('GAlab1forIntB.dat', 'w')
for i in range(0, len(SrFonB)):
    new_file.write(f'{SrFonB[i]}\n')
new_file.close()
new_file = open('GAlab1forIntT.dat', 'w')
for i in range(0, len(SrFonT)):
    new_file.write(f'{SrFonT[i]}\n')
new_file.close()

FonTint = scipy.interpolate.interp1d (SrFonT, SrFonB)
FonBint = [] #список, в котором значения фонов, соответствующие по времени средним компам
for i in range(0, len(SrCompT)):
    FonBint.append(FonTint(SrCompT[i]))
#plt.plot(SrCompT, FonBint, '-ob')
#plt.show()
NB = []
for i in range(0, len(FonBint)):
    nB = round(SrCompB[i] - FonBint[i], 0)
    NB.append(nB)
print(NB)
print(len(FonBint), len(SrCompB), len(SrCompT), len(NB))
#plt.plot(SrCompT, NB)
#plt.show()

print(la*12/m.pi)
M = []
for i in range(0, len(SrCompT)):
    mk = (SrCompT[i] - Nh - 1 + la*12/m.pi)*ko
    S = S0 + mk
    t = S*m.pi/12 - al
    ms = (m.sin(fi)*m.sin(de) + m.cos(fi)*m.cos(de)*m.cos(t))**-1
    M.append(ms)
magn = []
for i in range(0, len(NB)):
    ma = -2.5*m.log(NB[i])
    magn.append(ma)
print(M)
plt.plot(M, magn)
plt.show()


