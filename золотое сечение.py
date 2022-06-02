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

iter = 0
first = (3 - s.sqrt(5))/2
second = (s.sqrt(5) - 1)/2
c = a + first*(b - a)
d = a + second*(b - a)
while b - a >= 2*eps:
    iter += 1
    y1 = f.subs({x: c})
    y2 = f.subs({x: d})
    if y2 > y1:
        b = d
        d = c
        c = a + first*(b - a)
    else:
        a = c
        c = d
        d = a + second*(b - a)
minx = float((a + b)/2)
miny = f.subs({x:minx})
print(f'Точка минимума этой функции: ({float(minx):.6f},{float(miny):.6f})')
print('Количество итераций:', iter)