import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import laplace
a = 2.5 
b = 2
x = np.random.laplace(a, b, 400)

#Хранение массива чисел
#fout = open ("Massiv2.txt", "w" ) 
#list = x.flatten().tolist()
#for list in x: 
#    fout.write (str(list)+"\n")

#Считывание из файла выборки значений
lin = [] 
with open("Massiv2.txt") as f:
    for line in f:
        lin.append([float(g) for g in line.split()])
v = np.array(lin)

# Создание гистограммы
num_bins = 10
count, bins, patches = plt.hist(v, num_bins, density=1, edgecolor = 'black', alpha=1)

# График теоретической плотности вероятности
x_axis = np.arange(-14, 15, 0.01)
plt.plot(x_axis, laplace.pdf(x_axis,a,b), linewidth=3, color='r')
plt.xticks(np.arange(min(x), max(x)+1, 5.0))
plt.xlabel('Значения выборки')
plt.ylabel('Вероятность')
plt.title(r'Гистограмма: a=2.5, b=2')
plt.subplots_adjust(left=0.15)
plt.show()