#f(x) = x^2 + 2(x*lg(x/e) - 2),   [1.5; 2], eps = 0.01
#ФИБОНАЧЧИ
import sympy as s
from sympy import *
print('***Метод Фибоначчи***')
print('Введите начало интервала:')
a = float(input())
print('Введите конец интервала:')
b = float(input())
print('Введите погрешность:')
eps = float(input())

x = Symbol('x', real = True)
f = x**2 + 2*(x*s.log(x/s.exp(1), 10) - 2)

fib = [0]*51
fib[0] = 1
fib[1] = 1
for i in range (2, 50):
    fib[i] = fib[i-1] + fib[i-2]
print('Введите вещественное число из интервала (0,1):')
alpha = float(input())

f1 = (b - a)*(alpha + 1)/(2*eps)
i = 0
while (fib[i] < f1):
    i += 1
n = i - 1
k = i - 3
it = 0
flag = True
for j in range(n, 1, -1):
    c = a + (b - a) * fib[j-1]/fib[j+1]
    d = a + (b - a) * fib[j]/fib[j+1]
    if (c == d):
        do.something()
    elif (c > d):
        a = c
        c = d
        flag = True
    elif (c < d):
        d = c
        b = d
        flag = False
    it += 1
if flag:
    d = d + alpha * (b-a)/fib[n+1]
else:
    d = d - alpha * (b-a)/fib[n+1]
if f.subs({x:c})>f.subs({x:d}):
    x_min = (d + c)/2
else:
    x_min = (c + a)/2
print(f'Точка минимума: ({x_min:.6f}, {float(f.subs({x: x_min})):.6f})')
print(f'Количество итераций: {it}')
