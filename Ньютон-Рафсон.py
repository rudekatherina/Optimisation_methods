import sympy as s
from sympy import *
print('***Метод Ньютона-Рафсона***')
print('Введите начало интервала:')
a = float(input())
print('Введите конец интервала:')
b = float(input())
print('Введите погрешность:')
eps = float(input())

x0 = a
x = Symbol('x', real=True)

f = x*x + 2*(x*s.log(x/s.exp(1), 10) - 2)
y1 = diff(f, x).subs({x: x0})
y2 = diff(diff(f,x), x).subs({x: x0})

it = 1
while abs(y1) > eps and x0 >= a:
    x1 = x0
    x0 = x0 - y1/y2
    y1 = diff(f, x).subs({x:x0})
    y2 = diff(diff(f, x), x).subs({x:x0})
    it += 1
minx = x1
print(f'Точка минимума: ({minx}, {float(f.subs({x: minx})):.6f})')
print('Количество итераций: ', it)