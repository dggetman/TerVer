import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import laplace
import math

a = 2.5

#Считывание из файла выборки значений
lin = []
with open("Massiv2.txt") as f:
    for line in f:
        lin.append([float(g) for g in line.split()])
x = np.array(lin)

b = [-3, -2, -1, 0, 1, 2, 3]
f = abs(x-b)
# График
plt.plot(x,f, '.')
#plt.plot(b, f, linewidth=3, color='r')
plt.xlabel('Значения выборки')
plt.ylabel('Значения функции')
plt.title(r'Поиск коэффициента b ММП')
plt.subplots_adjust(left=0.15)
plt.show()