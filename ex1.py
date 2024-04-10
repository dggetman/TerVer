import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# Задание 1
from scipy.stats import norm

a = 1.6  # исходное матожидание
sigma = 9.1 ** 0.5  # исходная дисперсия
x = np.random.normal(a, sigma, 425)
# Хранение массива чисел
#fout = open ("Massiv.txt", "w" )
#list = x.flatten().tolist()
#for list in x:
#   fout.write (str(list)+"\n")
# Считывание из файла выборки значений
lin = []
with open("Massiv.txt") as f:
    for line in f:
        lin.append([float(g) for g in line.split()])
v = np.array(lin)
# Создание гистограммы
num_bins = 10
count, bins, patches = plt.hist(v, num_bins, density=1, edgecolor='black', alpha=1)
# График теоретической плотности вероятности
x_axis = np.arange(-9, 12, 0.001)
plt.plot(x_axis, norm.pdf(x_axis, a, sigma), linewidth=3, color='r')
plt.xticks(np.arange(min(x), max(x) + 1, 5.0))
plt.xlabel('Значения выборки')
plt.ylabel('Вероятность')
plt.title(r'Гистограмма: a=1.6, $\sigma=9.1$')
plt.subplots_adjust(left=0.15)
plt.show()

