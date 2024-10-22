import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import scipy
from scipy.optimize import curve_fit
import astropy.io.fits as pyfits
def singlegraffits(a):
    All = []
    #открываем фитс файл
    hdul = pyfits.open(f'{a}')
    scidata = hdul[0].data
    exp = hdul[0].header['exptime']
    d = hdul[0].data
    bias = 1000
    return d

d = singlegraffits("C:/Users/ivank/PycharmProjects/pythonProject1/obj-sky.fts")
plt.imshow(d, origin='lower', cmap='gray_r')
plt.show()
# Define the Gaussian function
# def gaussian(x, a, mu, sigma):
#    return a * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
#
# # Sample data
# x_data = [6619.76, 6620.6, 6621.44, 6622.28, 6623.12, 6623.96, 6624.8, 6625.64, 6626.48, 6627.32, 6628.16, 6629.0, 6629.84, 6630.68, 6631.52, 6632.36, 6633.2, 6634.04, 6634.88]
#
# y_data = [1.73242e-17, 1.3834e-17, 1.46976e-17, 1.49556e-17, 2.97337e-17, 5.55667e-17, 1.09065e-16, 1.63835e-16, 1.9541e-16, 1.96996e-16, 1.69607e-16, 1.31709e-16, 9.4509e-17, 6.08026e-17, 3.79065e-17, 2.60252e-17, 2.10381e-17, 1.89794e-17, 1.51363e-17]
# Center = x_data[y_data.index(max(y_data))]
# print(Center)
# shiftx = []
# for i in range(len(x_data)):
#     shiftx.append(x_data[i] - Center)
# y_data = np.array(y_data)/max(y_data)
# Maxsh = max(shiftx)
# shiftx = np.array(shiftx)/max(shiftx)
# print(Maxsh)
#
# Y = []
# for i in range(len(shiftx)):
#     Y.append(0.99203953 * np.exp(-(shiftx[i] + 0.0180749) ** 2 / (2 * 0.29623846 ** 2)))
# print(Y)
# plt.scatter(shiftx, Y, label = 'Test data')
# x = 0
# a = 0
# mu = 0
# sigma = 0
# popt, mesg = curve_fit(gaussian, shiftx, y_data)
# gaussian(shiftx, * popt)
# # Plotting the original data and the fitted curve
# plt.scatter(shiftx, y_data, label = 'Original data')
# plt.plot(shiftx, gaussian(shiftx, * popt), color = 'red', label = 'Fitted curve')
# print(gaussian(shiftx, * popt))
# print(popt[1]*Maxsh + Center)
# plt.legend()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Gaussian Curve Fitting')
# plt.show()

