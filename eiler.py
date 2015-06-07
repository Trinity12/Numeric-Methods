from math import cos
from math import sqrt

def Eiler(f, h, y, t):
    return y + h * f(t, y)

def f(t, y):
    return t + cos(y / sqrt(5))

y0, t0, h, tmax = 2.6, 1.8, 0.1, 2.9
y, t = y0, t0
while t <= tmax:
    print("t = " + str(t) + "   " + "y = " + str(y))
    y = Eiler(f, h, y, t)
    t += h
