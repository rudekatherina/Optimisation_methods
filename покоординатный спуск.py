from sympy import *
import math
x, x1, x2, l = symbols('x x1 x2 l')
f, g, h = symbols('f g h', cls=Function)
f = 2*x1**2 + x2**2 + x1*x2 + x1 + x2
print (expand(f))
x1_0=0
x2_0=0
s1=x1_0
s2=x2_0
def down(f,x1_0,x2_0,k):
    x_1,x_2, x1, x2, l = symbols('x_1 x_2 x1 x2 l')
    "первый орт с + и с -"
    F1=False
    x_1=1
    x_2=0
    if (f.subs({x1:x1_0+k*x_1,x2:x2_0+k*x_2})<f.subs({x1:x1_0,x2:x2_0})):
        x1_0=x1_0+k*x_1
        x2_0=x2_0+k*x_2
        F1=True
    else:
        if (f.subs({x1:x1_0-k*x_1,x2:x2_0-k*x_2})<f.subs({x1:x1_0,x2:x2_0})):
            x1_0=x1_0-k*x_1
            x2_0=x2_0-k*x_2
            F1=True
        "проверка отрицательного значения"

    "второй орт с + и с - "
    F2=False
    x_1=0
    x_2=1
    if (f.subs({x1:x1_0+k*x_1,x2:x2_0+k*x_2})<f.subs({x1:x1_0,x2:x2_0})):
        x1_0=x1_0+k*x_1
        x2_0=x2_0+k*x_2
        F2=True
    else:
        if (f.subs({x1:x1_0-k*x_1,x2:x2_0-k*x_2})<f.subs({x1:x1_0,x2:x2_0})):
            x1_0=x1_0-k*x_1
            x2_0=x2_0-k*x_2
            F2=True
    if F1==False and F2==False:
        k=k/2
        return down(f,x1_0,x2_0,k)
    else:
        if (s1-x1_0)**2+(s2-x2_0)**2<E*E:
            d={x1_0:x2_0}
            print (s1,s2)
            return d
        else: return down(f,x1_0,x2_0,k)



print(down(f,x1_0,x2_0,1))
