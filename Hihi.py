import math as m
import matplotlib.pyplot as plt
H = 50
g = 10
u = 5
v = 5
b = m.pi/4
A = []
C = []
D = []
#for t in range(1000):
  #T.append(t/100)

for a in range(1000):
  for t in range(10000):
    f = round((v*m.sin(a*m.pi/2000)*t/1000), 1)
    g = round((v*m.cos(a*m.pi/2000)*t/1000), 1)
    #F.append(f)
    #G.append(g)
    y = round((H - u*m.cos(b)*t/1000), 1)
    x = round((u*m.sin(b)*t/1000), 1)
    #X.append(x)
    #Y.append(y)
    if f == y and g == x:
      C.append(y)
    if f == y and g == x:
      D.append(x)
      #print(f,g,t/1000, a*m.pi/2000)
      A.append(a*m.pi/2000)
#for i in range(0,len(T)):
  #while X[i] != F[i] and Y[i] != G[i]:
    #C.append(F[i])
plt.xlim([0,60])
plt.ylim([0,80])
plt.scatter(D,C)
plt.show()
#print(D)
#print(C)
print(A[round((len(A))/2)])