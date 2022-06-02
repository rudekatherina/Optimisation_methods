#КАСАТЕЛЬНЫЕ
import sympy as s
from sympy import *
print('***Метод касательных***')
print('Введите начало интервала:')
a = float(input())
print('Введите конец интервала:')
b = float(input())
print('Введите погрешность:')
eps = float(input())

x = Symbol('x', real=True)

f = x*x + 2*(x*s.log(x/s.exp(1), 10) - 2)

it = 0
y1 = diff(f, x).subs({x: a})
y2 = diff(f, x).subs({x: b})
if y1 >=0:
    minx = a
    miny = f.subs({x: a})
    it =+ 1
elif y2<=0:
    minx = b
    miny = f.subs({x: b})
    it = + 1
else:
    while abs(b - a) > eps:
        yd1 = diff(f, x).subs({x: a})
        yd2 = diff(f, x).subs({x: b})
        c = (y1 - y2 + b*yd2 - a*yd1)/(yd2 - yd1)
        y3 = f.subs({x:c})
        if y3 > 0:
            b = c
            it = + 1
        elif y3 < 0:
            a = c
            it = + 1
        else:
            it = + 1
        if abs(diff(c)) <= eps:
            break
    minx = c
    miny = f.subs({x: minx})
print(f'Точка минимума: ({minx}, {float(miny):.6f})')
print('Количество итераций: ', it)