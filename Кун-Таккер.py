from sympy import *
print('***Метод Куна-Таккера***')

x = Symbol('x', real = True)
y = Symbol('y', real = True)
L1 = Symbol('L1', real = True)
L2 = Symbol('L2', real = True)
L3 = Symbol('L3', real = True)
L4 = Symbol('L4', real = True)
L5 = Symbol('L5', real = True)

f = 2*x**2 + 3*y**2 - 40*x - 48*y
#Зададим ограничения g_i, вытекающие из заданного многоугольника, при этом x и y положительны
# из этого же многоугольника
g1 = 5*y - 4*x - 20
g2 = 5*y + 4*x - 60
g3 = 4*x - 4*y - 24
g4 = -x
g5 = -y
#Сформируем уравнения из производных по каждой переменной

a1 = diff(f, x) + L1*diff(g1, x) + L2*diff(g2, x) + L3*diff(g3, x) + L4*diff(g4, x) + L5*diff(g5, x)
a2 = diff(f, y) + L1*diff(g1, y) + L2*diff(g2, y) + L3*diff(g3, y) + L4*diff(g4, y) + L5*diff(g5, y)

sol1 = [] #список решений систем. Так как у нас пять ограничений, то мы будем иметь 2^5 = 32 системы
#1
sol = solve([a1, a2, L1, L2, L3, L4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <= 0 \
            and g2.subs({x: float(sol[x]), y: float(sol[y])}) <= 0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <= 0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <= 0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <= 0:
        sol1.append(sol)
#2
sol = solve([a1, a2, g1, g2, g3, g4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if float(sol[L1]) >= 0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L3]) >= 0 \
            and float(sol[L4]) >= 0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#3
sol = solve([a1, a2, L1, g2, g3, g4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if float(sol[L2]) >= 0 \
            and float(sol[L3]) >=0 \
            and float(sol[L4]) >= 0 \
            and float(sol[L5]) >= 0 \
            and g1.subs({x: float(sol[x]), y: float(sol[y])}) <= 0:
        sol1.append(sol)
#4
sol = solve([a1, a2, g1, L2, g3, g4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if float(sol[L1]) >= 0 \
            and float(sol[L3]) >=0 \
            and g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L4]) >= 0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#5
sol = solve([a1, a2, g1, g2, L3, g4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if float(sol[L1]) >= 0 \
            and float(sol[L2]) >=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L4]) >= 0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#6
sol = solve([a1, a2, g1, g2, g3, L4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if float(sol[L1]) >= 0 \
            and float(sol[L2]) >=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L3]) >= 0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#7
sol = solve([a1, a2, g1, g2, g3, g4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if float(sol[L1]) >= 0 \
            and float(sol[L2]) >=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L3]) >= 0 \
            and float(sol[L4]) >= 0:
        sol1.append(sol)
#8
sol = solve([a1, a2, L1, L2, g3, g4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L5]) >= 0 \
            and float(sol[L3]) >= 0 \
            and float(sol[L4]) >= 0:
        sol1.append(sol)
#9
sol = solve([a1, a2, L1, g2, L3, g4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L5]) >= 0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L4]) >= 0:
        sol1.append(sol)
#10
sol = solve([a1, a2, L1, g2, g3, L4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L5]) >= 0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L3]) >= 0:
        sol1.append(sol)
#11
sol = solve([a1, a2, L1, g2, g3, g4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L4]) >= 0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L3]) >= 0:
        sol1.append(sol)
#12
sol = solve([a1, a2, L1, L2, L3, g4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L4]) >= 0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#13
sol = solve([a1, a2, g1, L2, L3, g4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L5]) >= 0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L4]) >= 0:
        sol1.append(sol)
#14
sol = solve([a1, a2, g1, L2, g3, L4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L5]) >= 0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L3]) >= 0:
        sol1.append(sol)
#15
sol = solve([a1, a2, g1, L2, g3, g4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L4]) >= 0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L3]) >= 0:
        sol1.append(sol)
#16
sol = solve([a1, a2, g1, g2, L3, L4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#17
sol = solve([a1, a2, g1, g2, L3, g4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L4]) >= 0:
        sol1.append(sol)
#18
sol = solve([a1, a2, g1, g2, g3, L4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L3]) >= 0:
        sol1.append(sol)
#19
sol = solve([a1, a2, L1, L2, g3, L4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L3]) >= 0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#20
sol = solve([a1, a2, L1, L2, g3, g4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L3]) >= 0 \
            and float(sol[L4]) >= 0:
        sol1.append(sol)
#21
sol = solve([a1, a2, L1, g2, L3, L4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#22
sol = solve([a1, a2, L1, g2, L3, g4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L4]) >= 0:
        sol1.append(sol)
#23
sol = solve([a1, a2, L1, g2, g3, L4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L2]) >= 0 \
            and float(sol[L3]) >= 0:
        sol1.append(sol)
#24
sol = solve([a1, a2, g1, L2, L3, L4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#25
sol = solve([a1, a2, g1, L2, L3, g4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L4]) >= 0:
        sol1.append(sol)
#26
sol = solve([a1, a2, g1, g2, L3, L4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L2]) >= 0:
        sol1.append(sol)
#27
sol = solve([a1, a2, g1, L2, g3, L4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L1]) >= 0 \
            and float(sol[L3]) >= 0:
        sol1.append(sol)
#28
sol = solve([a1, a2, L1, L2, L3, L4, g5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L5]) >= 0:
        sol1.append(sol)
#29
sol = solve([a1, a2, L1, L2, L3, g4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L4]) >= 0:
        sol1.append(sol)
#30
sol = solve([a1, a2, L1, L2, g3, L4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L3]) >= 0:
        sol1.append(sol)
#31
sol = solve([a1, a2, L1, g2, L3, L4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g1.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L2]) >= 0:
        sol1.append(sol)
#32
sol = solve([a1, a2, g1, L2, L3, L4, L5], (x, y, L1, L2, L3, L4, L5))
if sol != []:
    if g2.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g3.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g4.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and g5.subs({x: float(sol[x]), y: float(sol[y])}) <=0 \
            and float(sol[L1]) >= 0:
        sol1.append(sol)
n = len(sol1)
#В списке удовлетворяющих системам решений найдем то, в котором будет минимум функции
#в данном нам многоугольнике
minx = (float(sol1[0][x]), float(sol1[0][y]))
minf = f.subs({x: float(sol1[0][x]), y: float(sol1[0][y])})
for i in range(1, n):
    if f.subs({x: sol1[i][x], y: sol1[i][y]}) < minf:
        minx = (float(sol1[i][x]), float(sol1[i][y]))
        minf = f.subs({x: float(sol1[i][x]), y: float(sol1[i][y])})
print(f'Минимальная точка {minx}')
print(f'Значение функции = {float(minf):.6f}')

