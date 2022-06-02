# f(x) = 2x1^2 + x2^2 + x1x2 + x1 + x2;         x0 = (0; 0)         min = (-0.1429; 0.4286)
import math
from sympy import *

print('****Ускоренный градиентный спуск p-го порядка****')
print('Первая координата:')
x0 = int(input())
print('Вторая координата:')
y0 = int(input())
print('Погрешность:')
eps = float(input())

x1 = Symbol('x1', real=True)
x2 = Symbol('y1', real=True)
alpha = Symbol('alpha', real=True)

f = 2*x1**2 + x2**2 + x1*x2 + x1 + x2 # - обрабатываемая функция

def gold(f, a, b, eps):             # Вводим функцию одномерной минимизации по алгоритму
    first = (3 - math.sqrt(5)) / 2  # золотого сечения
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

x01 = x0
y01 = y0
it = 0
while (sqrt(diff(f, x1) ** 2 + diff(f, x2) ** 2)).subs({x1: x0, x2: y0}) >= eps: # Критерий остановки - номра градиента
    for i in range(0, 2):                                                        # не должна превышать погрешность
        f1 = f.subs({x1: x0 - alpha * (diff(f, x1)).subs({x1: x0, x2: y0}),
                     x2: y0 - alpha * (diff(f, x2)).subs({x1: x0, x2: y0})})
        alpha0 = gold(f1, -1, 1, eps)
        t0 = x0
        t1 = y0
        x0 = x0 - alpha0 * (diff(f, x1)).subs({x1: t0, x2: t1})
        y0 = y0 - alpha0 * (diff(f, x2)).subs({x1: t0, x2: t1})
        it += 1   # С 46 по 53 строку мы совершаем 2 шага по методу МНГС
    x02 = x0 - x01
    y02 = y0 - y01
    f2 = f.subs({x1: x01 + alpha* x02, x2: y01 + alpha*y02})  # Совершаем одномерную минимизацию в направлении
    a0 = gold(f2, -0.5, 0.5, eps)                             # (x0 - x01; y0-yo1)
    x0 = x0 + a0 * x02
    y0 = y0 + a0 * y02
it += 1

print('Координаты точки минимума: (',x0,',',y0,')')
print('Количество итераций:',it)
