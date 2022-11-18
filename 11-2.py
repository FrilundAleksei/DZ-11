# Даны две функции:
# f(x) = x^3 - 50x и g(x) = -x^4 + 88x^2 - 241
# Требуется:
# 1. Найти точки пересечения этих функций.
# 2. Построить графики функций в одной системе координат
# 3. Построить график общей функции


from sympy import *

x = Symbol('x')
fx=x**3-50*x
gx=-x**4+88*x**2-241

inters = solve(fx-gx, x)
inters_x=[]
for i in inters:
    z=round(i.n(), 4)
    inters_x.append(z)
inters_y=[]
for i in inters_x:
    y1=fx.subs(x, i)
    inters_y.append(y1)

for i, (x,y) in enumerate(zip(inters_x, inters_y), start = 1):
    print(f"Точка пересечения №{i} заданных функций : ({x}, {y})")

plot(fx, gx)
plot(fx-gx)

