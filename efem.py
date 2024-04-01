import math as m
import matplotlib.pyplot as plt
#import sympy as sp
import scipy.interpolate
import numpy as np

file = open("tau.dat", "r")
file_with_lines = file.readlines()[0:30]
all = []

for line in file_with_lines:
    a = line.split("   ")
    a = [x.strip('\n') for x in a]
    h = str(a).split()
    all.append(h)


for i in range(len(all)):
    H = all[i]
    for k in range(len(H)):
        all[i][k] = all[i][k].replace("вЂ™", "1")

print(all)

