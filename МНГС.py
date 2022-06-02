# f(x) = 2x1^2 + x2^2 + x1x2 + x1 + x2;         x0 = (0; 0)         min = (-0.1429; -0.4286)
import math
from sympy import *
print('***МНГС***')
print('Введите первую координату:')
x0 = int(input())
print('Введите вторую координату:')
y0 = int(input())
print('Введите погрешность:')
eps = float(input())

x1 = Symbol('x1', real=True)
x2 = Symbol('y1', real=True)
alpha = Symbol('alpha', real=True)

f = 2*x1**2 + x2**2 + x1*x2 + x1 + x2

def gold(f, a, b, eps):

    first = (3 - math.sqrt(5)) / 2
    second = (math.sqrt(5) - 1) / 2
    c = float(a + first * (b - a))
    d = float(a + second * (b - a))
    func = float(f.subs(alpha, c))
    fund = float(f.subs(alpha, d))
    while b - a >= 2 * eps:
        if fund > func:
            b = d
            d = c
            fund = func
            c = float(a + first * (b - a))
            func = float(f.subs(alpha, c))
        else:
            a = c
            c = d
            func = fund
            d = float(a + second * (b - a))
            fund = float(f.subs(alpha, d))
        minx = float((a + b) / 2)
    return minx

it = 1
while (sqrt(diff(f, x1) ** 2 + diff(f, x2) ** 2)).subs({x1: x0, x2: y0}) >= eps:
    f1 = f.subs({x1: x0 + alpha * (diff(f, x1)).subs({x1: x0, x2: y0}), x2: y0 + alpha * (diff(f, x2)).subs({x1: x0, x2: y0})})
    alpha0 = gold(f1, -1, 1, eps)
    t0 = x0
    t1 = y0
    x0 = x0 + alpha0 * (diff(f, x1)).subs({x1: t0, x2: t1})
    y0 = y0 + alpha0 * (diff(f, x2)).subs({x1: t0, x2: t1})
    it += 1
print(f'Минимальная точка: {x0}, {y0}')
print('Количество итераций:',it)


