import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import scipy
from scipy.optimize import curve_fit
import pylab
#функция, читающая тхт файлы с одномерным графиком
def Read_Two_Column_File(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))

    return x, y
#гауссиана
def gaussian(x, a, mu, sigma):
   return a * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))

#ищет центр по аппроксимации гауссианой и рисует график для наглядности
def LookingCenter(start_point, finish_point, x_list, y_list, a, b, c):
    x_data = []
    y_data = []
    #выбираем наш отрезок
    for i in range(len(x_list)):
        if start_point < x_list[i] < finish_point:
            x_data.append(x_list[i])
            y_data.append(y_list[i])
    #это х координата неаппроксимированного пика
    Center = x_data[y_data.index(max(y_data))]
    #чтобы аппроксимировать без проблем смещаем наши точки в окружение нуля
    shiftx = []
    for i in range(len(x_data)):
        shiftx.append(x_data[i] - Center)
    #также, чтобы не было ругани с curve_fit - нормируем данные на максимальные
    y_data = np.array(y_data) / max(y_data)
    Maxsh = max(shiftx)
    shiftx = np.array(shiftx) / max(shiftx)
    #аппроксимируем
    popt, mesg = curve_fit(gaussian, shiftx, y_data)
    gaussian(shiftx, *popt)
    # Plotting the original data and the fitted curve
    # plt.scatter(shiftx*Maxsh + Center, y_data, label='Original data', linewidth=0.8, color='blue')
    # plt.plot(shiftx*Maxsh + Center, gaussian(shiftx, *popt), color='red', label='Fitted curve', linewidth=0.8)
    # #print(gaussian(shiftx, *popt))
    print(f"The Wavelength of peak center after approximation: {popt[1] * Maxsh + Center}")
    print(f"The Wavelength of peak center before appoximation: {Center}")

    pylab.subplot(a, b, c)
    pylab.plot(shiftx*Maxsh + Center, gaussian(shiftx, *popt), color='red', label='Fitted curve', linewidth=0.8)
    pylab.scatter(shiftx * Maxsh + Center, y_data, label='Original data', linewidth=0.8, color='blue')
    pylab.plot([popt[1] * Maxsh + Center, popt[1] * Maxsh + Center], [0, max(gaussian(shiftx, *popt))], linewidth=0.6,
             label=f'{popt[1] * Maxsh + Center}')
    pylab.plot([Center, Center], [0, max(y_data)], linewidth=0.6, label=f'{Center}')
    #pylab.title("Линейный график")
    pylab.xlabel('Wavelength, A')
    pylab.ylabel('Flow')
    pylab.title('Gaussian Curve Fitting')
    pylab.legend()


