import math as m
import matplotlib.pyplot as plt

def func1():
  k1x = - K*vx0[-1]*(vx0[-1]**2 + vy0[-1]**2)**0.5/m
  K1x.append(k1x)
def func2():
  k1y = - g - K*vy0[-1]*(vy0[-1]**2 + vx0[-1]**2)**0.5/m
  K1y.append(k1y)
def func3():
  k2x = - K*(vx0[-1]+h/2)*((vx0[-1]+h/2)**2 + ((vy0[-1]+K1x[-1]*h/2)**2))**0.5/m
  K2x.append(k2x)
def func4():
  k2y = -g - K*(vy0[len(vy0)-1]+h/2)*((vx0[len(vx0)-1]+h/2)**2 + ((vy0[-1]+K1y[-1]*h/2)**2))**0.5/m
  K2y.append(k2y)
def func5():
  k3x = - K*(vx0[-1]+h/2)*((vx0[-1]+h/2)**2 + (vy0[-1]+K2x[-1]*h/2)**2)**0.5/m
  K3x.append(k3x)
def func6():
  k3y = - g - K*(vy0[-1]+h/2)*((vx0[-1]+h/2)**2 + (vy0[-1]+K2y[-1]*h/2)**2)**0.5/m
  K3y.append(k3y)
def func7():
  k4x = - K*(vx0[-1]+h)*((vx0[-1]+h)**2 + (vy0[-1]+K3x[-1]*h)**2)**0.5/m
  K4x.append(k4x)
def func8():
  k4y = - g - K*(vy0[-1]+h)*((vx0[-1]+h)**2 + (vy0[-1]+K3y[-1]*h)**2)**0.5/m
  K4y.append(k4y)
H = 1.5 #Начальная высота
g = 10 #Ускорение свободного падения
m = 5 #Масса
K = 0.1 #Коэф сопротивления
vx0 = [2] #Список, где сидят скорости по х
vy0 = [1] #Список, где скорости по у
h = 0.5 #Шаг, по которому смотрим изменение
#Далее группа списков для коэффициентов
K1x = []
K1y = []
K2x = []
K2y = []
K3x = []
K3y = []
K4x = []
K4y = []
#Далее списки, куда вносится модуль скорости и номера итерации (время, по сути)
V = []
I = []
#Далее списки, куда вносятся проекции скоростей, для построения графиков, для проверки
VxForSing = []
VyForSing = []
for i in range(0,10):
  func1()
  func2()
  func3()
  func4()
  func5()
  func6()
  func7()
  func8()
  vx = vx0[-1] + h*(K1x[-1] + 2*K2x[-1] + 2*K3x[-1] + K4x[-1])/6
  vy = vy0[-1] + h*(K1y[-1] + 2*K2y[-1] + 2*K3y[-1] + K4y[-1])/6
  vx0.append(vx)
  vy0.append(vy)
  VxForSing.append(vx)
  VyForSing.append(vy)
  v = (vx**2 + vy**2)**0.5
  V.append(v)
  I.append(i)
print(vx0)
print(vy0)
print(K1x, K1y, K2x, K2y, K3x, K3y, K4x, K4y)
print(V)
print(I)
plt.scatter(I, V)
plt.show()