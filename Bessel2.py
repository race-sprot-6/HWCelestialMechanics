import math as m
import matplotlib.pyplot as plt


def fJ(k, e):
    j = 1/p*(k*e/2)**k*Summb[-1]/k*m.sin(k*M)
    J.append(j)

def fS(a, k, e, f, g):
    s = (-1) ** b * (k * e / 2) ** (2 * b) / (f * g)
    S.append(s)

M = 0.00146116
S = [0]
J = [0]
Summb = [0]
g = 1
f = 1
p = 1
Summ = [0]
Summk = [0]
for k in range(1, 10):

    for b in range(10):
        f = f * (b + 1)  # f, g - факториалы
        g = g * (b + 1 + k)
        #m = m * (k + 1)
        fS(b, k, 0.1, f, g)
        SummF = S[-1] + Summb[-1]
        Summb.append(SummF)
        #print(f, g)
    p = p*(k+1)
    fJ(k, 0.1)
    SummF2 = J[-1] + Summk[-1]
    Summk.append(SummF2)
#print(Summk[-1])

E = M + 2*Summk[-1]
print(E)

def fE():
  E1 = M1 +e*m.sin(Elist[-1])
  Elist.append(E1)
e = 0.011
th = 10+25/60
T0 = 9+10/60
Elist = [0.00146116]
M1 = 0.00146116
for k in range(50):
  fE()
print(Elist[-1])

