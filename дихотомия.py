import sympy as s
from sympy import *

print('Введите начало рассматриваемого интервала:')
a = float(input())
print('Введите конец рассматриваемого интервала:')
b = float(input())
print('Введите погрешность:')
eps = float(input())
print('Введите число дельта:')
delta = float(input())

x = Symbol('x', real=True)

f = x*x + 2*(x*s.log(x/s.exp(1), 10) - 2)

iter = 0
while b - a >= 2*eps:
    iter += 1
    c = (a+b)/2 - delta/2
    d = (a+b)/2 + delta/2
    y1 = f.subs({x:c})
    y2 = f.subs({x:d})
    if y1 > y2:
        a = c
    else:
        b = d
minx = (a + b)/2
miny = f.subs({x:minx})
print(f'Точка минимума этой функции: ({minx},{float(miny):.6f})')
print('Количество итераций:', iter)
