#ХОРДЫ
import sympy as s
from sympy import *
print('***Метод хорд***')
print('Введите начало интервала:')
x1 = float(input())
print('Введите конец интервала:')
x2 = float(input())
print('Введите погрешность:')
eps = float(input())

x = Symbol('x', real=True)

f = x*x + 2*(x*s.log(x/s.exp(1), 10) - 2)

it = 1
flag = True
x3 = x2 - (x2 - x1)*diff(f, x).subs({x:x2}) / (diff(f, x).subs({x:x2}) - diff(f, x).subs({x:x1}))
if x1 > x3:
    minx = x1
    flag = False
elif x2 < x3:
    minx = x2
    flag = False
elif flag:
    while abs(diff(f, x).subs({x:x3})) > eps:
        x1 = x2
        x2 = x3
        x3 = x2 - (x2 - x1)*diff(x2) / (diff(x2) - diff(x1))
        it += 1
        if x1 > x3:
            minx = x1
            flag = False
            break
        elif x2 < x3:
            minx = x2
            flag = False
            break
else:
    minx = x3
print(f'Точка минимума: ({minx}, {float(f.subs({x: minx})):.6f})')
print('Количество итераций: ', it)
