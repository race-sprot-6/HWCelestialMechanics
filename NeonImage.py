import astropy.io.fits as pyfits
from astropy.wcs import WCS
import astropy
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from statistics import mean
import configparser
import os
from ApproxGauss import Read_Two_Column_File
from ApproxGauss import gaussian
from ApproxGauss import LookingCenter
from scipy.optimize import curve_fit
from scipy import stats
import pylab
import math as m
import matplotlib.ticker as ticker
def singlegraffits(a):
    All = []
    #открываем фитс файл
    hdul = pyfits.open(f'{a}')
    scidata = hdul[0].data
    exp = hdul[0].header['exptime']
    d = hdul[0].data

    bias = 1000
    TwoDSpec = []
    for i in range(len(d[0])):
        A = []
        for j in range(491, 541):
            A.append(d[j][i])
        avr = sum(A)/50 - bias
        All.append(avr)
    for i in range(441, 591):
        TwoDSpec.append(d[i])

    # plt.imshow(TwoDSpec, origin='lower')
    # plt.grid(color='white', ls='solid')
    # plt.show()
    return [All, TwoDSpec]

#функция, которая считыввет тхт файл с двумя столбцами и строит одномерный график

All = []
Pixels = []


ADU1 = np.array(singlegraffits("C:/Users/ivank/PycharmProjects/pythonProject1/s240717/t0201.fts")[0])

ADU2 = np.array(singlegraffits("C:/Users/ivank/PycharmProjects/pythonProject1/s240717/t0202.fts")[0])

ADUSumm = []
for i in range(len(ADU1)):
    ADUSumm.append((ADU1[i] + ADU2[i])/2000)
    #ADUSumm[i] = m.log(ADUSumm[i])
    Pixels.append(i)
A1 = [3893.23, 4045.97, 4183.11, 4191.04, 4200.90, 4259.74, 4334.12, 4345.64, 4387.98]
P1 = [412, 616, 788, 800, 811, 883, 972, 987, 1037]
A2 = [4425.40, 4471.50, 4537.95, 4545.04, 4579.35, 4713.61, 4735.91, 4752.73, 4764.86, 4789.53, 4806.02, 4818.06, 4837.31, 4847.81, 4864.33, 4885.09, 4921.93, 4957.03, 5005.34, 5015.68, 5037.75, 5047.74, 5060.73, 5080.46, 5116.50, 5145.03, 5162.03, 5188.43, 5204.08, 5221.86]
P2 = [1080, 1135, 1212, 1220, 1261, 1411, 1436, 1453, 1469, 1495, 1516, 1526, 1537, 1548, 1577, 1601, 1640, 1679, 1731, 1741, 1766, 1776, 1790, 1812, 1850, 1881, 1899, 1927, 1943, 1963]
A3 = [5330.78, 5341.79, 5360.01, 5373.05, 5400.64, 5420.16, 5433.65, 5495.87, 5506.11, 5560.57, 5572.54, 5606.73, 5656.66, 5689.93, 5719.23, 5748.3, 5764.42, 5804.45, 5820.16, 5852.43, 5875.64, 5903.34, 5944.83, 5975.01, 5988.32, 6000.93, 6030.00, 6044.48, 6074.34, 6096.16, 6118.01, 6128.45, 6143.06, 6163.59, 6182.15, 6217.18, 6246.73, 6266.50, 6293.81, 6304.79]
P3 = [2077, 2088, 2108, 2122, 2150, 2170, 2184, 2249, 2259, 2317, 2329, 2364, 2415, 2450, 2480, 2510, 2526, 2567, 2583, 2616, 2640, 2669, 2711, 2741, 2755, 2767, 2797, 2814, 2841, 2863, 2887, 2898, 2912, 2932, 2952, 2987, 3017, 3037, 3065, 3076]
A4 = [6334.43, 6351.86, 6382.99, 6402.25, 6444.71, 6506.53, 6532.68, 6598.95, 6678.15, 6717.04, 6752.83, 6871.29, 6929.47, 6965.43, 7032.41, 7065.71, 7147.04, 7173.94, 7245.17]
P4 = [3106, 3123, 3155, 3175, 3217, 3281, 3307, 3374, 3455, 3495, 3531, 3653, 3712, 3749, 3817, 3852, 3938, 3965, 4038]
A = [5689.93, 5719.23, 5748.3, 5764.42, 5804.45, 5820.16, 5852.43, 5875.64, 5903.34, 5944.83, 5975.01, 5988.32, 6000.93, 6030.00, 6044.48, 6074.34, 6096.16, 6118.01, 6128.45, 6143.06, ]
Pix = [2450, 2479.5, 2567, 2526, 2567, 2583, 2616.13, 2911.92]

name = A1+A2+A3+A4
pix = P1+P2+P3+P4
A1str, A2str, A3str, A4str = [], [], [], []
for i in range(len(A1)):
    A1str.append(str(A1[i]))
for i in range(len(A2)):
    A2str.append(str(A2[i]))
for i in range(len(A3)):
    A3str.append(str(A3[i]))
for i in range(len(A4)):
    A4str.append(str(A4[i]))
Pix1, Pix2, Pix3, Pix4 = [], [], [], []
ADUSumm1, ADUSumm2, ADUSumm3, ADUSumm4 = [], [], [], []
TwoDSpec1, TwoDSpec2, TwoDSpec3, TwoDSpec4 = [], [], [], []
for i in range(len(Pixels)):
    if Pixels[i] < max(P1)+70:
        Pix1.append(Pixels[i])
        ADUSumm1.append(ADUSumm[i])
    if max(P1) < Pixels[i] < max(P2)+70:
        Pix2.append(Pixels[i])
        ADUSumm2.append(ADUSumm[i])
    if max(P2) < Pixels[i] < max(P3)+70:
        Pix3.append(Pixels[i])
        ADUSumm3.append(ADUSumm[i])
    if max(P3) < Pixels[i] < max(P4)+70:
        Pix4.append(Pixels[i])
        ADUSumm4.append(ADUSumm[i])
for j in range(250):
    TwoDSpec1.append(np.log(ADUSumm))

# for j in range(50):
#     TwoDSpec2.append(ADUSumm2)
# for j in range(50):
#     TwoDSpec3.append(ADUSumm3)
# for j in range(50):
#     TwoDSpec4.append(ADUSumm4)
# plt.subplot(2, 1, 1)
# plt.imshow(TwoDSpec1, origin='lower')
# plt.yticks([])
# plt.xticks([])
# plt.axis([0, 4112, 0, 50])
# plt.axis([0, 1032, 0, 50])
# plt.axis([0, 1032, 0, 50])
#plt.axis([0, 1032, 0, 50])
#plt.grid(color='white', ls='solid')
#plt.show()
#TwoDSpec = np.array(singlegraffits("C:/Users/ivank/PycharmProjects/pythonProject1/s240717/t0201.fts")[1])
# plt.subplot(2, 1, 2)
# plt.plot(Pix1, ADUSumm1, label = "Neon VPHG1200@540", linewidth=0.5, color='black')
# #
# plt.xticks([])
# for P1, A1str in zip(P1, A1str):
#     plt.axvline(x=P1, ymin = 0, ymax = 0.8, color='black', linestyle='-', linewidth=0.3)
#     plt.text(P1, 1500, A1str, rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8)
# #plt.xlabel('Pixels')
# plt.ylabel('ADU')
# #plt.title('Spectrum Neon')
# plt.axis([0, 1100, 0, 1700])
# plt.show()

# plt.plot(Pix2, ADUSumm2, label = "Neon VPHG1200@540", linewidth=0.5, color='black')
# plt.xticks([])
# for P2, A2str in zip(P2, A2str):
#     plt.axvline(x=P2, ymin = 0, ymax = 0.75, color='black', linestyle='-', linewidth=0.3)
#     plt.text(P2, 13000, A2str, rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8)
# #plt.xlabel('Pixels')
# plt.ylabel('ADU')
# plt.title('Spectrum Neon')
# plt.axis([1050, 2000, 0, 15000])
# plt.show()
#
# plt.plot(Pix3, ADUSumm3, label = "Neon VPHG1200@540", linewidth=0.5, color='black')
# for P3, A3str in zip(P3, A3str):
#     plt.axvline(x=P3, ymin = 0, ymax = 0.8, color='black', linestyle='-', linewidth=0.3)
#     plt.text(P3, 45000, A3str, rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8)
# #plt.xlabel('Pixels')
# plt.ylabel('ADU')
# plt.title('Spectrum Neon')
# plt.axis([2000, 3135, 0, 50000])
# plt.show()
#
# plt.plot(Pix4, ADUSumm4, label = "Neon VPHG1200@540", linewidth=0.5, color='black')
# for P4, A4str in zip(P4, A4str):
#     plt.axvline(x=P4, ymin = 0, ymax = 0.8, color='black', linestyle='-', linewidth=0.5)
#     plt.text(P4, 42000, A4str, rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8)
# #plt.xlabel('Pixels')
# plt.ylabel('ADU')
# plt.title('Spectrum Neon')
# plt.axis([3080, 4112, 0, 46000])
# plt.show()
A1n, A2n, A3n, A4n, = [], [], [], []
P1n, P2n, P3n, P4n, = [], [], [], []
for i in range(len(A1)):
    if ADUSumm[P1[i]] > 0.24:
        A1n.append(A1str[i])
        P1n.append(P1[i])
print(len(A1n))
print(len(A1))
for i in range(len(A2)):
    if ADUSumm[P2[i]] > 0.8:
        A2n.append(A2str[i])
        P2n.append(P2[i])
print(len(A2n))
print(len(A2))
for i in range(len(A3)):
    if ADUSumm[P3[i]] > 2:
        A3n.append(A3str[i])
        P3n.append(P3[i])
print(len(A3n))
print(len(A3))
for i in range(len(A4)):
    if ADUSumm[P4[i]] > 3:
        A4n.append(A4str[i])
        P4n.append(P4[i])

fig, ax = plt.subplots(2, 1, constrained_layout=True)
fig. tight_layout ()

#plt.subplot(2, 1, 1)
ax[0].imshow(TwoDSpec1, origin='lower', cmap='gray_r')
ax[0].set_title('Spectrum Neon, VPHG1200@540')
ax[0].set_xlabel('')
ax[0].set_ylabel('')
xax = ax[0].axes.get_xaxis()
xax = xax.set_visible(False)
yax = ax[0].axes.get_yaxis()
yax = yax.set_visible(False)
ax[0].set_position([0.074, 0.3, 0.885, 0.5])

#ax[0].yticks([])
#ax[0].xticks([])
#plt.axis([0, 1100, 0, 50])
# plt.axis([0, 1032, 0, 50])
# plt.axis([0, 1032, 0, 50])
#plt.axis([0, 1032, 0, 50])
#plt.grid(color='white', ls='solid')
#plt.show()
#TwoDSpec = np.array(singlegraffits("C:/Users/ivank/PycharmProjects/pythonProject1/s240717/t0201.fts")[1])
#plt.subplot(2, 1, 2)
ax[1].plot(Pixels, ADUSumm, label = "Neon VPHG1200@540", linewidth=0.5, color='black')
ax[1].axis([0, 4112, 0, 27])

ax[1].set_xlabel('Pixels')
ax[1].set_ylabel('ADU/1000')


for P1n, A1n in zip(P1n, A1n):
    ax[1].axvline(x=P1n, ymin = 0, ymax = 0.8, color='black', linestyle='-', linewidth=0.5)
    ax[1].text(P1n, 24, A1n, rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=5)
for P2n, A2n in zip(P2n, A2n):
    ax[1].axvline(x=P2n, ymin = 0, ymax = 0.8, color='black', linestyle='-', linewidth=0.5)
    ax[1].text(P2n, 24, A2n, rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=5)
for P3n, A3n in zip(P3n, A3n):
    ax[1].axvline(x=P3n, ymin = 0, ymax = 0.8, color='black', linestyle='-', linewidth=0.5)
    ax[1].text(P3n, 24, A3n, rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=5)
for P4n, A4n in zip(P4n, A4n):
    ax[1].axvline(x=P4n, ymin = 0, ymax = 0.8, color='black', linestyle='-', linewidth=0.5)
    ax[1].text(P4n, 24, A4n, rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=5)

plt.show()

