from sympy import *
import matplotlib.pyplot as plt
import math
x, x1, x2, l = symbols('x x1 x2 l')
f, g, h = symbols('f g h', cls=Function)
f = 2*x1**2 + x2**2 + x1*x2 + x1 + x2
print (expand(f))
x1_0=1
x2_0=1
s1=x1_0
s2=x2_0
def devisor(a,b,c,d,g):
    if (b-a<=2*E):
        return ((a+b)/2)
    else:
        if (g(c)<=g(d)):
            b=d
            d=c
            c=((3-math.sqrt(5))/2*(b-a)+a)
        else:
            a=c
            c=d
            d=((math.sqrt(5)-1)/2*(b-a)+a)
        return(devisor(a,b,c,d,g))

def down(f,x1_0,x2_0,k):
    x, x1, x2, l = symbols('x x1 x2 l')
    "первая переменная "
    F1=False
    g=f.subs({x1:x1_0+k*l,x2:x2_0})
    c=((3-math.sqrt(5))/2*4-1)
    d=((math.sqrt(5)-1)/2*(3+1)-1)
    l=devisor(-1,3,c,d,g)
    x=x1_0+l*k
    if (f.subs({x1:x,x2:x2_0})<f.subs({x1:x1_0,x2:x2_0})):
        x1_0=x
        F1=True
    else:
        x=x1_0-l*k
        if (f.subs({x1:x,x2:x2_0})<f.subs({x1:x1_0,x2:x2_0})):
            x1_0=x
            F1=True
        else: x=x1_0
        "проверка отрицательного значения"
    "вторая переменная "
    F2=False
    g=f.subs({x1:x1_0,x2:x2_0+l*k})
    c=((3-math.sqrt(5))/2*4-1)
    d=((math.sqrt(5)-1)/2*(3+1)-1)
    l=devisor(-1,3,c,d,g)
    x=x1_0+l*k
    if (f.subs({x1:x1_0,x2:x})<f.subs({x1:x1_0,x2:x2_0})):
        x2_0=x
        F2=True
    else:
        x=x2_0-l*k
        if (f.subs({x1:x1_0,x2:x})<f.subs({x1:x1_0,x2:x2_0})):
            x2_0=x
            F2=True
        else:
            x=x2_0
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

