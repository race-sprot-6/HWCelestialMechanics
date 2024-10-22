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
    file_with_lines = file.readlines()[0:32]
    all = []
    oll = []
    for line in file_with_lines:
        a = line.split(" ")
        a = [x.strip('\n') for x in a]
        h = str(a).split()
        all.append(h)
    for i in range(len(all)):
        all[i][0] = all[i][0].replace('[', '')
        all[i][0] = all[i][0].replace('"', '')
        all[i][0] = all[i][0].replace("'", '')
        all[i][0] = all[i][0].replace(']', '')
        if 0 <= int(all[i][0]) <= 253:
            oll.append(int(all[i][0]))
        else:
            print(f'Erorr. Max Value = 253 and Min Value = 0')
            oll.append(253)
    return oll

#функция, где находим спектры отдельных диодов
def singlegraf(a):
    #открываем фитс файл
    hdul = pyfits.open(f'C:/Users/ivank/PycharmProjects/pythonProject1/SpecDiod/leds{a}.fts')

    scidata = hdul[0].data
    exp = hdul[0].header['exptime']
    d = hdul[0].data

    conf = config('leds550G.cfg')
    bias = 1000
    All = []
    for i in range(len(d[0])):
        A = []
        for j in range(491, 541):
            A.append(d[j][i])
        avr = sum(A)/50 - bias
        All.append(avr*conf[int(a)]*12/(exp*253))


    kak, nikak = [], []

    #строим красивый спектр
    #plt.imshow(d, origin='lower')
    # plt.grid(color='white', ls='solid')
    # plt.show()

    for i in range(len(All)):
        nikak.append(i)
    #строим не красивый спектр
    plt.plot(nikak, All, label = f'{[int(a)]}')
    #plt.text(1500, 3000, f"{a}")

    #plt.legend(loc="upper left")
    #plt.show()
    return All

bias = 1000
file1 = open("leds.txt", "w")
file1 = open("leds.txt", "a")
ADU, N = [], []
for i in range(10):
    All = singlegraf(f'0{i}')
    file1.write(str(All) +"\n")

for i in range(10, 31):
    All = singlegraf(f'{i}')
    file1.write(str(All) + "\n")
file1.close()

file1 = open("leds.txt", "r")
file_with_lines = file1.readlines()[0:31]
all = []

for line in file_with_lines:
    a = line.split(" ")
    a = [x.strip('\n') for x in a]
    h = str(a).split()
    all.append(h)
for i in range(len(all)):
    for k in range(len(all[i])):
        all[i][k] = all[i][k].replace(',', '')
        all[i][k] = all[i][k].replace('"', '')
        all[i][k] = all[i][k].replace("'", '')
        all[i][k] = all[i][k].replace(']', '')
        all[i][k] = all[i][k].replace('[', '')

Summ = []
for i in range(2080):
    add = []
    for j in range(31):
        add.append(float(all[j][i]))
    summ = sum(add)
    Summ.append(summ)

for i in range(len(Summ)):
    N.append(i)

#тут можно посмотреть разницу между моим и измеренным спектром
# hdul1 = pyfits.open('C:/Users/ivank/PycharmProjects/pythonProject1/s22230203.fts')
# #hdul.info()
# scidata = hdul1[0].data
# exp1 = hdul1[0].header['exptime']
# print("exp=", exp1)
# d1 = hdul1[0].data
# All1 = []
# for i in range(len(d1[0])):
#     A = []
#     for j in range(491, 541):
#         A.append(d1[j][i])
#         #print(i)
#     avr = sum(A)/50 - bias
#     All1.append(avr)

#plt.plot(N, All1)

plt.plot(N, Summ)
plt.xlabel('X, px')
plt.ylabel('ADU ')
plt.title('Flat Spectre')
#plt.legend(loc='best', fontsize=5)
plt.show()