import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import scipy
from scipy.optimize import curve_fit
from ApproxGauss import Read_Two_Column_File
from ApproxGauss import gaussian
from ApproxGauss import LookingCenter
import pylab
import astropy.io.fits as pyfits
from statistics import mean


def beatxt(file): # функция, которая подчищает данные из тхт файла
    file1 = open(f"{file}", "r")
    file_with_lines = file1.readlines()[0:1032]
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
            all[i][k] = float(all[i][k])
    return all

def findnoise1(filefts1):

    # открываем фитс файл
    hdul = pyfits.open(f'{filefts1}')
    scidata = hdul[0].data
    exp = hdul[0].header['exptime']
    d = hdul[0].data

    # делаем тхт файл, куда сложим отсчёты из фитс
    file1 = open("ftsin.txt", "w")
    file1 = open("ftsin.txt", "a")

    for i in range(len(d)):
        ADU = []
        for k in range(len(d[0])):

            ADU.append(d[i][k])
        file1.write(str(ADU) + "\n")

    file1.close()

    all = beatxt("ftsin.txt")

    # выбираем три области, где будут проходить усреднения и уследняем
    Cut1, Cut2, Cut3 = [], [], []
    M1, M2, M3 = [], [], []
    NoiseL = []

    Cuti1 = all[90:110] # выбрали из снимка полосу с 90-й по 110-ю строки
    for i in range(len(Cuti1)):
        #Cut1.append(Cuti1[i][10:30]) # выбрали из полоски квадрат с 10-го до 30-го столбца
        M1.append(mean(Cuti1[i][10:30]))
    NoiseL.append(mean(M1))

    Cuti2 = all[30:60]
    for i in range(len(Cuti2)):
        #Cut2.append(Cuti2[i][130:160])
        M2.append(mean(Cuti2[i][130:160]))
    NoiseL.append(mean(M2))

    Cuti3 = all[130:160]
    for i in range(len(Cuti3)):
        #Cut3.append(Cuti3[i][130:160])
        M3.append(mean(Cuti3[i][130:160]))
    NoiseL.append(mean(M3))

    print(f'Average values of ADU in three areas:{NoiseL}')
    return np.array(NoiseL)

def findnoise2(filefts1):

    # открываем фитс файл
    hdul = pyfits.open(f'{filefts1}')
    scidata = hdul[0].data
    exp = hdul[0].header['exptime']
    d = hdul[0].data

    # делаем тхт файл, куда сложим отсчёты из фитс
    file1 = open("ftsin.txt", "w")
    file1 = open("ftsin.txt", "a")

    for i in range(len(d)):
        ADU = []
        for k in range(len(d[0])):

            ADU.append(d[i][k])
        file1.write(str(ADU) + "\n")

    file1.close()

    all = beatxt("ftsin.txt")

    # выбираем три области, где будут проходить усреднения и уследняем
    Cut1, Cut2, Cut3 = [], [], []
    M1, M2, M3 = [], [], []
    ThreeADU = []

    Cuti1 = all[90:110] # выбрали из снимка полосу с 90-й по 110-ю строки
    for i in range(len(Cuti1)):
        Cut1.append(Cuti1[i][10:30]) # выбрали из полоски квадрат с 10-го до 30-го столбца
    AADU1 = []
    for i in range(len(Cut1)):
        for k in range(len(Cut1[0])):
            AADU1.append(Cut1[i][k])
    ThreeADU.append(np.array(AADU1))
        #M1.append(mean(Cuti1[i][10:30]))
    #NoiseL.append(mean(M1))

    Cuti2 = all[30:60]
    for i in range(len(Cuti2)):
        Cut2.append(Cuti2[i][130:160])
    AADU2 = []
    for i in range(len(Cut2)):
        for k in range(len(Cut2[0])):
            AADU2.append(Cut2[i][k])
        ThreeADU.append(np.array(AADU2))
        #M2.append(mean(Cuti2[i][130:160]))
    #NoiseL.append(mean(M2))

    Cuti3 = all[130:160]
    for i in range(len(Cuti3)):
        Cut3.append(Cuti3[i][130:160])
    AADU3 = []
    for i in range(len(Cut3)):
        for k in range(len(Cut3[0])):
            AADU3.append(Cut3[i][k])
        ThreeADU.append(np.array(AADU3))
        #M3.append(mean(Cuti3[i][130:160]))
    #NoiseL.append(mean(M3))


    #print(f'Average values of ADU in three areas:{NoiseL}')
    return ThreeADU

NoiseL1 = findnoise1("C:/Users/ivank/IDLWorkspace71/FitsFiles/s240708/s22230301.fts")
NoiseL2 = findnoise1("C:/Users/ivank/IDLWorkspace71/FitsFiles/s240708/s22230302.fts")

print(f'Noise of ADU in three areas. Var1:{abs(NoiseL1-NoiseL2)}')

ThreeADU1 = findnoise2("C:/Users/ivank/IDLWorkspace71/FitsFiles/s240708/s22230301.fts")
ThreeADU2 = findnoise2("C:/Users/ivank/IDLWorkspace71/FitsFiles/s240708/s22230302.fts")

Noise1, Noise2, Noise3 = [], [], []
#for i in range(len(ThreeADU1)):
Noise1 = mean(ThreeADU1[0] - ThreeADU2[0])
Noise2 = mean(ThreeADU1[1] - ThreeADU2[1])
Noise3 = mean(ThreeADU1[2] - ThreeADU2[2])

print(f'Noise of ADU in three areas. Var2:{abs(Noise1), abs(Noise2), abs(Noise3)}')