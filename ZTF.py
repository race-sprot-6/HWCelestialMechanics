from astroquery.vizier import Vizier
from astropy import units as u
import numpy as np
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
from ztfquery import lightcurve
import csv
from statistics import mean

# target = SkyCoord('21 34 20.3718881736 +47 38 00.205959228', unit=(u.hourangle, u.deg), frame='icrs')
#
# lcq = lightcurve.LCQuery.from_position(target.ra.deg, target.dec.deg, 3)
# lcq.show()
#
# lcq = lightcurve.LCQuery.from_position(target.ra.deg, target.dec.deg, 3)
# lcq.show()

filtcode, mjd, mag = [], [], []
with open('C:/Users/ivank/Documents/data.csv') as File:
    lines = csv.reader(File, delimiter=',')
    for row in lines:
        filtcode.append(row[8])
        mjd.append(row[4])
        mag.append(row[5])

for i in range(len(mjd)-2):
    if mjd[i] < mjd[i+1] > mjd[i+2]:
        ind = i+2
        break

mjd1, mjd2, mag1, mag2 = [], [], [], []
# for i in range(499):
#     mjd1.append(mjd[i])
# for i in range(500, len(mjd)):
#     mjd2.append(mjd[i])


for i in range(len(mjd)):
    if filtcode[i] == 'zg':
        mjd1.append(mjd[i])
        mag1.append(mag[i])
    elif filtcode[i] == 'zr':
        mjd2.append(mjd[i])
        mag2.append(mag[i])
Mjd, Mag = [], []
for i in range(len(mjd1)):
    for k in range(len(mjd2)):
        if round(float(mjd1[i]), 1) == round(float(mjd2[k]), 1) and 0.2 < float(mag1[i])-float(mag2[k]) < 0.550:
            Mjd.append((float(mjd1[i])+float(mjd2[k]))/2)
            Mag.append(float(mag1[i])-float(mag2[k]))
M = mean(Mag)
#полином 1 степени по функции
p = np.polyfit(Mjd, Mag, 1)
#подставляем значения x к полученному полиному
ya = np.polyval(p, Mjd)
print(len(Mjd), len(Mag))

print(M)
print(filtcode[499], filtcode[500])
print(filtcode)
print(mjd)
print(mag)
plt.scatter(Mjd, Mag, s = 5)
plt.plot(Mjd, ya)
plt.show()