# f(x) = 2x1^2 + x2^2 + x1x2 + x1 + x2;
import math
import numpy as np
from numpy import linalg
from sympy import *

print('****Модифицированный метод Ньютона****')
print('Первая координата:')
x0 = int(input())
print('Вторая координата:')
y0 = int(input())
print('Погрешность:')
eps = float(input())

x1 = Symbol('x1', real=True)
x2 = Symbol('y1', real=True)
alpha = Symbol('alpha', real=True)

f = 2*x1**2 + x2**2 + x1*x2 + x1 + x2 # обрабатываемая нами функция


# Начало создания матрицы вторых производных
mat = []
a = []
a.append(dfdx2)
a.append(dfdxy)
mat.append(a)
a = []
a.append(dfdyx)
a.append(dfdy2)
mat.append(a)
mat1 = np.matrix(mat).astype(float)

#Создана матрица вторых производных - далее ищем обратную ей матрицу:
matr = linalg.inv(mat1).astype(float)

# Найдем уравнение для поиска минимального альфа:
c1 = dfdx.subs({x1: x0, x2: y0}) #верхний элемент столбца значений частной производной в исходной точке
d1 = dfdy.subs({x1: x0, x2: y0}) #нижний элемент столбца значений частной производной в исходной точке
a = []
mat1 = []
a.append(c1)
mat1.append(a)
a = []
a.append(d1)
mat1.append(a)
mat1 = np.matrix(mat1).astype(float)
res = np.dot(matr, mat1) # получили матрицу 2*1 с коэффициентами для умножения на альфа из с1 и d1
k1 = res[0, 0].astype(float)
k2 = res[1, 0].astype(float)
f1 = f.subs({x1: x0 - alpha*k1, x2: y0 - alpha*k2})
#Ищем минимум найденной функции с помощью алгоритма золотого сечения:
a0 = gold(f1, -5, 5, eps)
xs = x0 - a0*k1
ys = y0 - a0*k2
print('Координаты точки минимума: (',xs,',',ys,')')

