#Минимальная точка (7.551020408163265, 5.959183673469388)
from sympy import *

print('***Метод внешних штрафов***')
print('Введите погрешность измерения H:')
eps = float(input())
print('Введите погрешность измерения нормы градиента φ:')
eps1 = float(input())

x = Symbol('x', real = True)
y = Symbol('y', real = True)
al = Symbol('al', real = True)

f = 2*x**2 + 3*y**2 - 40*x - 48*y
#Зададим ограничения g_i, вытекающие из заданного многоугольника, при этом x и y положительны
# из этого же многоугольника
g1 = 5*y - 4*x - 20
g2 = 5*y + 4*x - 60
g3 = 4*x - 4*y - 24
g4 = -x
g5 = -y

#Функция одномерной минимизации методом золотого сечения
def gold(f, a, b, eps):
    first = (3 - sqrt(5)) / 2
    second = (sqrt(5) - 1) / 2
    c = float(a + first * (b - a))
    d = float(a + second * (b - a))
    func = float(f.subs(al, c))
    fund = float(f.subs(al, d))
    while b - a >= 2 * eps:
        if fund > func:
            b = d
            d = c
            fund = func
            c = float(a + first * (b - a))
            func = float(f.subs(al, c))
        else:
            a = c
            c = d
            func = fund
            d = float(a + second * (b - a))
            fund = float(f.subs(al, d))
        minx = float((a + b) / 2)
    return minx
#Функция для определения квадрата максимума из нуля и функции в точке (x0, y0)
def m(f, x0, y0):
    if f.subs({x: x0, y:y0}) > 0:
        return f.subs({x: x0, y:y0})
    else:
        return 0
x01 = 10 # Координаты
y01 = 10 # исходной точки
it = 0

r = 1
while m(g1, x01, y01)**2 + m(g2, x01, y01)**2 + m(g3, x01, y01)**2 + m(g4, x01, y01)**2 + m(g5, x01, y01)**2 > eps:
    ph = f + r * (g1**2 + g2**2 + g3**2 + g4**2 + g5**2)
    #Производные функции φ по x и по y соответственно
    phx = diff(f, x) + 2*r*(diff(g1, x)*m(g1, x01, y01) + diff(g2, x)*m(g2, x01, y01) + \
          diff(g3, x)*m(g3, x01, y01) + diff(g4, x)*m(g4, x01, y01) + diff(g5, x)*m(g5, x01, y01))
    phy = diff(f, y) + 2*r*(diff(g1, y)*m(g1, x01, y01) + diff(g2, y)*m(g2, x01, y01) + \
          diff(g3, y)*m(g3, x01, y01) + diff(g4, y)*m(g4, x01, y01) + diff(g5, y)*m(g5, x01, y01))
    while sqrt(phx**2 + phx**2).subs({x: x01, y: y01}) > eps:
    #Ищем x-овую и y-овую координаты с альфа
        a1 = (x01 - al*phx).subs({x: x01, y: y01})
        a2 = (y01 - al*phy).subs({x: x01, y: y01})

        #Вписываем найденные координаты в уравнения g1, g2, g3
        g11 = g1.subs({x: a1, y: a2})
        g12 = g2.subs({x: a1, y: a2})
        g13 = g3.subs({x: a1, y: a2})
        g14 = g4.subs({x: a1, y: a2})
        g15 = g5.subs({x: a1, y: a2})
        #Далее рассматриваем 32 случая, где от значения альфа
        #зависит решение системы
        amin = 1000
        #1
        s = (f + r * (g1 ** 2 + g2**2 + g3**2 + g4**2 + g5**2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) > 0 \
        and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) > 0:
            amin = a0
        #2
        s = f.subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #3
        s = (f + r * (g1 ** 2 + g2 ** 2 + g3 ** 2 + g4 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #4
        s = (f + r * (g1 ** 2 + g2 ** 2 + g3 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #5
        s = (f + r * (g1 ** 2 + g2 ** 2 + g4 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #6
        s = (f + r * (g1 ** 2 + g3 ** 2 + g4 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #7
        s = (f + r * (g2 ** 2 + g3 ** 2 + g4 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #8
        s = (f + r * (g1 ** 2 + g2 ** 2 + g3**2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #9
        s = (f + r * (g1 ** 2 + g2 ** 2 + g4**2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #10
        s = (f + r * (g1 ** 2 + g3 ** 2 + g4 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #11
        s = (f + r * (g2 ** 2 + g3 ** 2 + g4 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #12
        s = (f + r * (g1 ** 2 + g2 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #13
        s = (f + r * (g1 ** 2 + g3 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #14
        s = (f + r * (g2 ** 2 + g3 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #15
        s = (f + r * (g1 ** 2 + g4 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #16
        s = (f + r * (g2 ** 2 + g4 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #17
        s = (f + r * (g3 ** 2 + g4 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #18
        s = (f + r * (g1 ** 2 + g2 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #19
        s = (f + r * (g1 ** 2 + g3 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #20
        s = (f + r * (g1 ** 2 + g4 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #21
        s = (f + r * (g1 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #22
        s = (f + r * (g2 ** 2 + g3 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #23
        s = (f + r * (g2 ** 2 + g4 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #24
        s = (f + r * (g2 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #25
        s = (f + r * (g3 ** 2 + g4 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0})<= 0 and a0 < amin:
            amin = a0
        #26
        s = (f + r * (g3 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #27
        s = (f + r * (g4 ** 2 + g5 ** 2)).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        #28
        s = (f + r * g1 ** 2).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) > 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #29
        s = (f + r * g2 ** 2).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) > 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #30
        s = (f + r * g3 ** 2).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) > 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        #31
        s = (f + r * g4 ** 2).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) > 0 and g15.subs({al: a0}) <= 0 and a0 < amin:
            amin = a0
        # 32
        s = (f + r * g5 ** 2).subs({x: a1, y: a2})
        a0 = gold(s, -2, 2, eps1)
        if g11.subs({al: a0}) <= 0 and g12.subs({al: a0}) <= 0 and g13.subs({al: a0}) <= 0 \
                and g14.subs({al: a0}) <= 0 and g15.subs({al: a0}) > 0 and a0 < amin:
            amin = a0
        x01 = a1.subs({al: amin})
        y01 = a2.subs({al: amin})
        phx = diff(f, x) + 2 * r * (diff(g1, x) * m(g1, x01, y01) + diff(g2, x) * m(g2, x01, y01) + \
                                    diff(g3, x) * m(g3, x01, y01) + diff(g4, x) * m(g4, x01, y01) + \
                                    diff(g5, x) * m(g5, x01, y01))
        phy = diff(f, y) + 2 * r * (diff(g1, y) * m(g1, x01, y01) + diff(g2, y) * m(g2, x01, y01) + \
                                    diff(g3, y) * m(g3, x01, y01) + diff(g4, y) * m(g4, x01, y01) + \
                                    diff(g5, y) * m(g5, x01, y01))
        it += 1
    r *= 10
print(f'Точка минимума этой функции: ({x01}, {y01})')
print('Количество итераций:', it)









