import math as m
import matplotlib.pyplot as plt
#import sympy as sp
import scipy.interpolate
import numpy as np
import csv
import itertools
import re

def oshif(b,c):
    w = []
    f = []
    #ищу совпадения по символам и фасую
    for k in range(len(all)):
        kswk =[]
        for i in range(len(all[0])):
            string = str(all[k][i])
            x = re.search(b, string)
            if x != None:
                kswk.append(x.string)
            else:
                kswk.append(0)
        w.append(kswk)
    #print(a)
    #убираю нули
    for i in range(len(w)):
        for k in range(len(w[i])):
            k = len(w[i])-1
            if w[i][k] == 0:
                w[i].remove(0)
    # добавляю нужные нули и нужные символы
    for i in range(len(w)):
        if w[i] == []:
            f.append(0)
        else:
            f.append(w[i][0])
    #делаю красиво и чтоб потом работало (числа получаю)
    for i in range(len(f)):
        if f[i] != 0:
            f[i] = f[i].replace('[', '')
            f[i] = f[i].replace("'", '')
            f[i] = f[i].replace(',', '')
            f[i] = f[i].replace('+', '1')
            f[i] = f[i].replace('-', '-1')
            f[i] = f[i].replace(b, '')
        f[i] = int(f[i])
        if f[i] != 0:
            if f[i] > 100:
                f[i] = f[i] - 100
            if f[i] < -100:
                f[i] = f[i] + 100
            if 20 > f[i] > 10:
                f[i] = f[i] - 10
            if -20 < f[i] < -10:
                f[i] = f[i] + 10
    #c.append(f[i])
    return(f)
    #print(f)
def list(a,b):
    for i in range(len(ang[b])):
        a.append(ang[b][i])

def angf(a):
    x = ((ang[a][0] + ang[a][1]/60 +ang[a][2]/3600)*m.pi/180 + (ang[a][3]*t +ang[a][4]*t**2 + ang[a][5]*t**3 + ang[a][6]*t**4)/206265)
    return(x)
values = []
with open('tau.dat') as tau:
    for line in csv.reader(tau, delimiter=' '):
        values.append(map(int, line))
#print(values)

file = open("tau.dat", "r")
file_with_lines = file.readlines()[0:89]
all = []

for line in file_with_lines:
    a = line.split(" ")
    a = [x.strip('\n') for x in a]
    h = str(a).split()
    all.append(h)

for i in range(len(all)):
    H = all[i]
    for k in range(len(H)):
        all[i][k] = all[i][k].replace("вЂ™", "s")

for i in range(len(all)):
    H = all[i]
    for k in range(len(H)):
        all[i][k] = all[i][k].replace("ls", "ks")

for i in range(len(all)):
    H = all[i]
    for k in range(len(H)):
        all[i][k] = all[i][k].replace("Un", "An")

#print(all)
PS = []
PC = []
FS = []
FC = []
Per = []
for i in range(len(all)):
    for k in range(len(all[i])):
        all[i][k] = all[i][k].replace(',', '')
        all[i][k] = all[i][k].replace('"', '')
        all[i][k] = all[i][k].replace("'", '')
        all[i][k] = all[i][k].replace(']', '')
    if all[i][-1] == '-':
        PS.append(0)
    else:
        PS.append(float(all[i][-1]))
    if all[i][-2] == '-':
        PC.append(0)
    else:
        PC.append(float(all[i][-2]))
    if all[i][-3] == '-':
        FS.append(0)
    else:
        FS.append(float(all[i][-3]))
    if all[i][-4] == '-':
        FC.append(0)
    else:
        FC.append(float(all[i][-4]))
    if all[i][-5] == '-':
        Per.append(0)
    else:
        Per.append(float(all[i][-5]))
#print(PS)
#print(PC)
#print(FS)
l, ks, F, Ve, D, Om, Ea, U, Ma, Ju, W, An, Me =[], [], [], [], [], [], [], [], [], [], [], [], []
oshif('l', l)
print(oshif('l', l))
oshif('ks', ks)
oshif('F', F)
oshif('Ve', Ve)
oshif('D', D)
oshif('Om', Om)
oshif('Ea', Ea)
oshif('U', U)
oshif('Ma', Ma)
oshif('Ju', Ju)
oshif('W', W)
W.append(oshif('W', W))
oshif('An', An)
oshif('Me', Me)
print(oshif('Om', Om))
print(oshif('W', W))


file = open("lks.txt", "r")
file_with_lines = file.readlines()[0:7]
ang = []

for line in file_with_lines:
    a = line.split(" ")
    a = [x.strip('\n') for x in a]
    h = str(a).split()
    ang.append(h)

for i in range(len(ang)):
    H = ang[i]
    for k in range(len(H)):
        ang[i][k] = ang[i][k].replace("'в€’", "-")
        ang[i][k] = ang[i][k].replace("'", "")
        ang[i][k] = ang[i][k].replace("[", "")
        ang[i][k] = ang[i][k].replace("]", "")
        ang[i][k] = ang[i][k].replace(",", "")
        ang[i][k] = float(ang[i][k])
print(ang)

l1, ks1, T1, W3, om, F1, D1 = [], [], [], [], [], [], []
list(l1, 3)
list(ks1, 4)
list(T1, 1)
list(W3, 0)
list(om, 2)
list(F1, 5)
list(D1, 6)

for t in range(2):
    angf(0)
    print(angf(0))
tay1 = 0
tay2 = 0
T1 = []
T2 = []
for t in range(100):
    tay1 = 0.000036096 * t - 1.18037 * 10 ** (-5) * t ** 2 + 8.4863 * 10 ** (-7) * t ** 3 + tay1 + tay2
    for k in range(len(PC)):
        tay2 = tay2 + (FC[k] + PC[k]*t)*m.cos(oshif('W', W)[k]*angf(0)+oshif('l', l)[k]*angf(3)+oshif('ks', ks)[k]*angf(4)+oshif('F', F)[k]*angf(5)+oshif('D', D)[k]*angf(6)) +(FS[k] + PS[k]*t)*m.sin(oshif('W', W)[k]*angf(0)+oshif('l', l)[k]*angf(3)+oshif('ks', ks)[k]*angf(4)+oshif('F', F)[k]*angf(5)+oshif('D', D)[k]*angf(6))
        T2.append(tay2)
    T1.append(tay1)

T = []
for t in range(100):
    T.append(t)

plt.plot(T, T1)
plt.show()

