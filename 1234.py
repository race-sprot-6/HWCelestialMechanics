import math as m
import matplotlib.pyplot as plt

R = 6371
x = [7000.0]
y = [0.0]
vx = [0.0]
vy = [10.0]
g0 = 10**-2
gM = g0*R**2
h = 0.1

def fvx(vx, x, vy, y):
    r = (x**2 + y**2)**0.5
    return(-gM*x/(r**3))
def fx(vx, x, vy, y):
    return(vx)
def fvy(vx, x, vy, y):
    r = (x**2 + y**2)**0.5
    return(-gM*y/(r**3))
def fy(vx, x, vy, y):
    return (vy)

def fk1(vx, x, vy, y, a):
    if a == 1:
        return fvx(vx[-1], x[-1], vy[-1], y[-1])
    elif a == 2:
        return fx(vx[-1], x[-1], vy[-1], y[-1])
    elif a == 3:
        return fvy(vx[-1], x[-1], vy[-1], y[-1])
    elif a == 4:
        return fy(vx[-1], x[-1], vy[-1], y[-1])
def fk2(vx, x, vy, y, a):
    if a == 1:
        return fvx(vx[-1], x[-1] + h/2*fk1(vx, x, vy, y, 2), vy[-1], y[-1] + h/2*fk1(vx, x, vy, y, 4))
    elif a == 2:
        return fx(vx[-1] + h/2*fk1(vx, x, vy, y, 1), x[-1], vy[-1], y[-1])
    elif a == 3:
        return fvy(vx[-1], x[-1] + h/2*fk1(vx, x, vy, y, 2), vy[-1], y[-1] + h/2*fk1(vx, x, vy, y, 4))
    elif a == 4:
        return fy(vx[-1], x[-1], vy[-1] + h/2*fk1(vx, x, vy, y, 3), y[-1])
def fk3(vx, x, vy, y, a):
    if a == 1:
        return fvx(vx[-1], x[-1] + h/2*fk2(vx, x, vy, y, 2), vy[-1], y[-1] + h/2*fk2(vx, x, vy, y, 4))
    elif a == 2:
        return fx(vx[-1] + h/2*fk2(vx, x, vy, y, 1), x[-1], vy[-1], y[-1])
    elif a == 3:
        return fvy(vx[-1], x[-1] + h/2*fk2(vx, x, vy, y, 2), vy[-1], y[-1] + h/2*fk2(vx, x, vy, y, 4))
    elif a == 4:
        return fy(vx[-1], x[-1], vy[-1] + h/2*fk2(vx, x, vy, y, 3), y[-1])
def fk4(vx, x, vy, y, a):
    if a == 1:
        return fvx(vx[-1], x[-1] + h*fk3(vx, x, vy, y, 2), vy[-1], y[-1] + h*fk3(vx, x, vy, y, 4))
    elif a == 2:
        return fx(vx[-1] + h*fk3(vx, x, vy, y, 1), x[-1], vy[-1], y[-1])
    elif a == 3:
        return fvy(vx[-1], x[-1] + h*fk3(vx, x, vy, y, 2), vy[-1], y[-1] + h*fk3(vx, x, vy, y, 4))
    elif a == 4:
        return fy(vx[-1], x[-1], vy[-1] + h*fk3(vx, x, vy, y, 3), y[-1])
Nday = []
for n in range(200):
    Nday.append(n*3600)
X = []
Y = []
for t in range(60*60*24*3):
    #print(t)#секунды
    Summ_vx = vx[-1] +h/6*(fk1(vx, x, vy, y, 1) + 2*fk2(vx, x, vy, y, 1) + 2*fk3(vx, x, vy, y, 1) + fk4(vx, x, vy, y, 1))
    vx.append(Summ_vx)
    Summ_x = x[-1] + h/6*(fk1(vx, x, vy, y, 2) + 2 * fk2(vx, x, vy, y, 2) + 2 * fk3(vx, x, vy, y, 2) + fk4(vx, x, vy, y, 2))
    x.append(Summ_x)
    Summ_vy = vy[-1] + h/6*(fk1(vx, x, vy, y, 3) + 2 * fk2(vx, x, vy, y, 3) + 2 * fk3(vx, x, vy, y, 3) + fk4(vx, x, vy, y, 3))
    vy.append(Summ_vy)
    Summ_y = y[-1] + h/6*(fk1(vx, x, vy, y, 4) + 2 * fk2(vx, x, vy, y, 4) + 2 * fk3(vx, x, vy, y, 4) + fk4(vx, x, vy, y, 4))
    y.append(Summ_y)
    #if t == 3600:
        #X.append(Summ_x)
        #Y.append(Summ_y)
plt.scatter(x, y)
plt.show()
