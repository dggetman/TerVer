import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import multivariate_normal

n = 425
ax = 1.6
Dx = 9.1 ** 0.5
ay = 4.95
Dy = 3.4 ** 0.5
rxy = -0.6
alpha = 0.001
Dxy = rxy * Dx * Dy
cov = np.array([[Dx, Dxy], [Dxy, Dy]])
x = np.random.normal(ax, Dx, n)
y = np.random.normal(ay, Dy, n)
xc = []
yc = []
for i in range(n):
    c = np.random.multivariate_normal([x[i], y[i]], cov, size=n)
    xc.append([float(c[[i], [0]])])
    yc.append([float(c[[i], [1]])])
vxc = np.array(xc)
vyc = np.array(yc)
# Хранение массива чисел
xout = open("MassivX.txt", "w")
list = vxc.flatten().tolist()
for list in vxc:
    xout.write(str(list) + "\n")
xout.close()
yout = open("MassivY.txt", "w")
list = vyc.flatten().tolist()
for list in vyc:
    yout.write(str(list) + "\n")
yout.close()
# Вычисления
mx = sum(vxc) / n
print(mx)
my = sum(vyc) / n
print(my)
dx = sum((xi - mx) ** 2 for xi in vxc) / n
print(dx)
dy = sum((yi - my) ** 2 for yi in vyc) / n
print(dy)
sx = sum(vxc[i] - mx)
sy = sum(vyc[i] - my)
vrxy = (sx * sy) / ((dx * dy) ** 0.5)
print(vrxy)
rx = vrxy * ((dx / dy) ** 0.5) * (vyc - my) + ax
ry = vrxy * ((dy / dx) ** 0.5) * (vxc - mx) + ay
# Графики регрессии
plt.plot(vxc, vyc, '.')
plt.plot(vyc, rx, '-', color='r')
plt.plot(vxc, ry, '-', color='g')
plt.axis('equal')
plt.xticks(np.arange(min(x), max(x) + 1, 5.0))
plt.xlabel('Значения X')
plt.ylabel('Значения Y')
plt.title(r'Распределение и уравнения регрессий вектора (X,Y)')
plt.subplots_adjust(left=0.15)
plt.grid()
plt.show()
