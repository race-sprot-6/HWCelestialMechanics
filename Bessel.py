import math as m
import matplotlib.pyplot as plt
R = 6731


def fJ(k, e):
    j = 1/m*(k*e/2)**k*Summb[-1]/k
    J.append(j)

def fS(a, k, e, f, g):
    s = (-1) ** b * (k * e / 2) ** (2 * b) / (f * g)
    S.append(s)

M = 1.0
S = [0]
J = [0]
Summb = [0]
g = 1
f = 1
m = 1
Summ = [0]
Summk = [0]
for k in range(1, 5):

    for b in range(5):
        f = f * (b + 1)  # f, g - факториалы
        g = g * (b + 1 + k)
        #m = m * (k + 1)
        fS(b, k, 0.1, f, g)
        SummF = S[-1] + Summb[-1]
        Summb.append(SummF)
        #print(f, g)
    m = m*(k+1)
    fJ(k, 0.1)
    SummF2 = J[-1] + Summk[-1]
    Summk.append(SummF2)
print(Summk[-1])

E = M + 2*Summk[-1]
print(E)
for b in range(5):
    f = f * (b + 1)  # f, g - факториалы
    g = g * (b + 1 + k)
    # m = m * (k + 1)
    fS(b, k, 0.1, f, g)
    SummF = S[-1] + Summb[-1]
    Summb.append(SummF)
    print(f, g)
#print(1*m.sin())
XE = []
YE = []
for n in range(100):
    XE.append(R * m.cos(n * 10))
    YE.append(R * m.sin(n * 10))
