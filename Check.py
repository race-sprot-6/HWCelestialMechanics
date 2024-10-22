import astropy.io.fits as pyfits
from astropy.wcs import WCS
import astropy
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from statistics import mean

hdul = pyfits.open('C:/Users/ivank/PycharmProjects/pythonProject1/s22230203.fts')
#hdul.info()
scidata = hdul[0].data
exp = hdul[0].header['exptime']
print("exp=", exp)
d = hdul[0].data
#print(len(d[0]), len(d))

All = []
for i in range(len(d[0])):
    A = []
    for j in range(491, 541):
        A.append(d[j][i])
        #print(i)
    avr = sum(A)/50
    All.append(avr)
# print(len(d))
kak, nikak = [], []
# for i in range(len(d[516])):
#     if d[516][i] < 2000:
#         kak.append(d[516][i])
#     elif d[516][i] > 2000 and i < 1040:
#         for k in range(i, i+500):
#             kak.append(d[516][k])
#         break
#     elif d[516][i] > 2000 and i > 1040:
#         for k in range(i, len(d[516])):
#             kak.append(d[516][k])
#         break
# plt.imshow(d, origin='lower')
# plt.grid(color='white', ls='solid')
# plt.show()
#print(d[516])
max_adu = max(d[516])
ind = np.where(d[516] == max_adu)
# print(ind)
# ind = d[516].index(max_adu)
#print(len(d[0]), len(d))

# N = []
# ADU = []
# for i in range(len(d[516])):
#     N.append(i)
#     per = d[516][i] / exp
#     ADU.append(per)
for i in range(len(All)):
    nikak.append(i)
# print(N, ADU)
#local_maxima(N, ADU)
#plt.plot(N, ADU)
#plt.show()

plt.plot(nikak, All)
plt.show()

# def func(a):
#
#     a.append(2)
# A = []
# func(A)
#print(A)

import configparser
import os

def config(path):
    file = open(f"{path}", "r")
    file_with_lines = file.readlines()[1:33]
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

#oll = config('leds550G.cfg')
#print(len(oll))

