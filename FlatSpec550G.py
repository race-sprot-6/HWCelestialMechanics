import astropy.io.fits as pyfits
from astropy.wcs import WCS
import astropy
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

hdul = pyfits.open('C:/Users/ivank/PycharmProjects/pythonProject1/leds00.fts')
hdul.info()
scidata = hdul[0].data
exp = hdul[0].header['exptime']
print("exp=", exp)

d = hdul[0].data
print(d)
print(len(d[0]), len(d))

#plt.imshow(d, origin='lower')
#plt.grid(color='white', ls='solid')
#plt.show()

max_adu = max(d[516])
print(max_adu)

N = []
for i in range(len(d[516])):
    N.append(i)

plt.plot(N, d[516])
plt.show()
