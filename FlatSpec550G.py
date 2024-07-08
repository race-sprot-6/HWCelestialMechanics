import astropy.io.fits as pyfits
from astropy.wcs import WCS
import astropy
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from statistics import mean
import configparser
import os
def config(path):
    file = open(f"{path}", "r")
    file_with_lines = file.readlines()[2:33]
    all = []

    for line in file_with_lines:
        a = line.split(" ")
        a = [x.strip('\n') for x in a]
        h = str(a).split()
        all.append(h)


#функция, где находим спектры отдельных диодов. убираем вторые максимумы
def singlegraf(a):
    #открываем фитс файл
    hdul = pyfits.open(f'C:/Users/ivank/PycharmProjects/pythonProject1/SpecDiod/leds{a}.fts')
    #hdul.info()
    scidata = hdul[0].data
    exp = hdul[0].header['exptime']
    #print("exp=", exp)
    d = hdul[0].data
    #print(d)
    #print(len(d[0]), len(d))
    #убираем вторые максимумы там, где они есть

    All = []
    for i in range(len(d[0])):
        A = []
        for j in range(491, 541):
            A.append(d[j][i])
        avr = sum(A)/50
        All.append(avr/exp)
    kak, nikak = [], []
    # for i in range(len(d[516])):
    #     if d[516][i] < 2000:
    #         kak.append(d[516][i]/exp)
    #     elif d[516][i] > 2000 and i < 900:
    #         for k in range(i, i + 1100):
    #             kak.append(d[516][k]/exp)
    #         break
    #     elif d[516][i] > 2000 and i > 1140:
    #         for k in range(i, len(d[516])):
    #             kak.append(d[516][k]/exp)
    #         break
    # for i in range(len(d[516])):
    #     kak.append(d[516][i] / exp)

    #строим красивый спектр
    #plt.imshow(d, origin='lower')
    # plt.grid(color='white', ls='solid')
    # plt.show()

    #N = []
    #ADU = []
    #for i in range(len(d[516])):
        #N.append(i)
        #per = d[516][i]/exp
        #ADU.append(per)

    #plt.plot(N, ADU)
    #plt.show()
    for i in range(len(All)):
        nikak.append(i)
        #b.append(kak[i])
    #строим не красивый спектр
    plt.plot(nikak, All)
    #plt.show()
    #maxsingle = max(kak)
    #ADU.append(maxsingle)
    #ind = kak.index(maxsingle)
    #N.append(ind)


ADU, N = [], []
A, B, C, D, E = [], [], [], [], []
for i in range(9):
    singlegraf(f'0{i}')

for i in range(10, 31):
    singlegraf(f'{i}')

#plt.scatter(N, ADU)
plt.show()