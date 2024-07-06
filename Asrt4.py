import math as m
import matplotlib.pyplot as plt
#import sympy as sp
import scipy.interpolate
import numpy as np
import csv
import itertools

#values = []
#with open('phi.dat') as tau:
#    for line in csv.reader(tau, delimiter=' '):
#        values.append(map(int, line))
#print(values)

file = open("phi.dat", "r")
file_with_lines = file.readlines()[0:50]
all = []

for line in file_with_lines:
    a = line.split(" ")
    a = [x.strip('\n') for x in a]
    a = [x.strip('\t') for x in a]
    #print(a)
    all.append(a)
print(all)
All = []
ALL = []
for i in range(len(all)):
    alli = all[i][0].replace("\t", " " )
    All.append(alli)

for i in range(len(all)):
    alli = All[i].replace(",", ".")
    ALL.append(alli)
print(ALL)
s = 0

al = []
for i in range(len(ALL)):
    a = ALL[i].split()
    al.append(a)
print(al)
#print(al[0][0]+1)
for i in range(len(ALL)):
    if float(al[i][1]) > 0.31 and float(al[i][1]) < 0.83:
        s = (float(al[i][0]) - 27.32)*0.09 + s

print(s)

R = -3.07*s/(7.333-7.067) #0.197 - это дельта V
print(R)








