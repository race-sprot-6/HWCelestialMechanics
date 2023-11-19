import math as m
import matplotlib.pyplot as plt
#import sympy as sp
import scipy.interpolate
import numpy as np
def fpi(a, P, SM):
  pi = a/(P**2*(SM))**(1/3)
  PI.append(pi)

def fMv(mv, pi):
  Mv = mv + 5 + m.log10(pi)
  MV.append(Mv)
def fMb(Mv, BC):
  Mb = Mv + BC
  MB.append(Mb)
al1 = 21+6.9/60 #hour
de1 = 38+45/60 #grad
MV1 = [5.22, 6.04]
mv11 = 5.22
mv21 = 6.04
# Спектральный класс первой - K5V, второй - K7V
P1 = 722 #year
a1 = 24.65 #"
BC1 = [-0.60, -0.764]

al2 = 16+14.7/60
de2 = 33+52/60
MV2 = [5.58, 6.59]
mv21 = 5.58
mv22 = 6.59
# G0V, G1V
P2 = 1000.0
a2 = 6.60
BC2 = [-0.03, -0.038]

#SM = [2 ]

file = open("MagmMass.dat", "r")
file_with_lines = file.readlines()[0:30]
all = []

for line in file_with_lines:
    a = line.split("   ")
    a = [x.strip('\n') for x in a]
    all.append(a)
StEl = []
magn = []
mass = []

for i in range(0, int(len(all)/2)):
    StEl.append(all[2*i]+all[2*i+1])
for i in range(0, len(StEl)):
  for k in range(0, len(StEl[i])):
    StEl[i][k] = StEl[i][k].replace("вЂ“", "-" )
    StEl[i][k] = StEl[i][k].replace(" вЂ“", "-")
    StEl[i][k] = StEl[i][k].replace("+", "")
    StEl[i][k] = StEl[i][k].replace(" +", "")
    StEl[i][k] = StEl[i][k].replace(",", ".")
for i in range(0, len(StEl)):
  for k in range(0, len(StEl[i])):
    magn.append(float(StEl[i][1]))
    mass.append(float(StEl[i][0]))
P = []
SM =1
for j in range(0, 10):
    PI = []
    MV = []
    MB = []
    fpi(a1, P1, SM)
    P.append(PI[0])
    for i in range(0, len(MV1)):
        fMv(MV1[i], PI[0])

    for i in range(0, len(MV)):
        fMb(MV[i], BC1[i])

    MassInt = scipy.interpolate.interp1d(magn, mass)
    Mass = [] #список, в котором значения фонов, соответствующие по времени средним компам
    for i in range(0, len(MB)):
        sm = 10**(float(MassInt(MB[i])))
        Mass.append(sm)
    SM = Mass[0] + Mass[1]






print(StEl)
print(len(mass))
print(len(magn))
print(P[-1])
#plt.plot(mass, magn)
#plt.show()