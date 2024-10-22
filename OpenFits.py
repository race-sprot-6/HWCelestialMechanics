import astropy.io.fits as pyfits
from astropy.wcs import WCS
import astropy
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from statistics import mean
import configparser
import os

# открываем фитс файл
def singlegraf(a):
    hdul = pyfits.open(f'C:/Users/ivank/PycharmProjects/pythonProject1/SpecDiod/leds{a}.fts')
    file = open("leds.txt", "w")
    # file_with_lines = file.readlines()[0:89]

    scidata = hdul[0].data
    exp = hdul[0].header['exptime']
    # print("exp=", exp)
    d = hdul[0].data
    file = open("tau.dat", "r")
