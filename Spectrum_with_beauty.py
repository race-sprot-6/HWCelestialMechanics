import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import scipy
from scipy.optimize import curve_fit
from ApproxGauss import Read_Two_Column_File
from ApproxGauss import gaussian
from ApproxGauss import LookingCenter
import pylab

x, y = Read_Two_Column_File('C:/Users/ivank/IDLWorkspace71/FitsFiles/s240708/result_Dw1902+63/obj1_total.txt')

LookingCenter(6619, 6635, x, y, 2, 2, 1)
LookingCenter(6643, 6655, x, y, 2, 2, 3)
LookingCenter(6779, 6788, x, y, 1, 2, 2)
pylab.show()

#это у меня чтобы грязь по краям спектра подчистить
n = 60
del x[:n]
del y[:n]
for i in range(60):
    x.pop()
    y.pop()

plt.plot(x, y, linewidth=0.5, color='black', label = "Dw1902+63, Z = 0.0098")
plt.xlabel('Wavelength, Angstrom')
plt.ylabel('Flux, erg/sec')
#plt.text("Z = 0.0098 +- 0.0004")
plt.title('Spectrum Dw1902+63')
plt.legend()
plt.show()