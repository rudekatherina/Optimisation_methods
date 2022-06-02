import sympy as s
from sympy import *

print('Введите начало рассматриваемого интервала:')
a = float(input())
print('Введите конец рассматриваемого интервала:')
b = float(input())
print('Введите погрешность:')
eps = float(input())

x = Symbol('x', real=True)

f = x*x + 2*(x*s.log(x/s.exp(1), 10) - 2)
miny = f.subs({x:a})
minx = a
i = a
iter = 0
while i <= b:
    iter+=1
    y = f.subs({x: i})
    if y < miny:
        minx = i
        miny = y
    i += eps
print(f'Точка минимума этой функции: ({minx},{float(miny):.6f})')
print('Количество итераций:', iter)

