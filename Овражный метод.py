# f(x) = 2x1^2 + x2^2 + x1x2 + x1 + x2;         x0 = (0; 0)         min = (-0.1429; 0.4286)
import math
from sympy import *

print('****Овражный метод****')
print('Первая координата:')
x0 = int(input())
print('Вторая координата:')
y0 = int(input())
print('Погрешность:')
eps = float(input())
print('Отступ для x с волной:')
delta = float(input())

x1 = Symbol('x1', real=True)
x2 = Symbol('y1', real=True)
alpha = Symbol('alpha', real=True)

f = 2*x1**2 + x2**2 + x1*x2 + x1 + x2 #исследуемая функция

def gold(f, a, b, eps):                 #Используемая для одномерной минимизации функция
    first = (3 - math.sqrt(5)) / 2      #методом золотого сечения
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

def MSGD(x0, y0, eps):
    f1 = f.subs({x1: x0 - alpha * (diff(f, x1)).subs({x1: x0, x2: y0}),     #Функция для описания одного шага
                 x2: y0 - alpha * (diff(f, x2)).subs({x1: x0, x2: y0})})    # по МНГС
    alpha0 = gold(f1, -5, 5, eps)
    t0 = x0
    t1 = y0
    x0 = x0 - alpha0 * (diff(f, x1)).subs({x1: t0, x2: t1})
    y0 = y0 - alpha0 * (diff(f, x2)).subs({x1: t0, x2: t1})
    it = 1
    return [x0, y0, it]

x01 = x0
y01 = y0
it = 0
while (sqrt(diff(f, x1) ** 2 + diff(f, x2) ** 2)).subs({x1: x0, x2: y0}) >= eps:
    x01 = MSGD(x0, y0, eps)[0]      #делаем шаг по МНГС от начальной точки (x1-координата)
    y01 = MSGD(x0, y0, eps)[1]      #делаем шаг по МНГС от начальной точки (x2-координата)
    xw = MSGD(x0 + delta, y0 + delta, eps)[0] #делаем шаг по МНГС от точки с отступом delta (х1)
    yw = MSGD(x0 + delta, y0 + delta, eps)[1] #делаем шаг по МНГС от точки с отступом delta (х2)
    it += 1
    x02 = xw - x01  #определяем направление одномерной минимизации
    y02 = yw - y01
    f2 = f.subs({x1: x01 + alpha* x02, x2: y01 + alpha*y02})
    a0 = gold(f2, -5, 5, eps)   #минимизация этой функции по методу золотого сечения
    x0 = x01 + a0 * x02
    y0 = y01 + a0 * y02

print('The minimum point is (',x0,',',y0,')')
print('The number of iterations is:',it)
