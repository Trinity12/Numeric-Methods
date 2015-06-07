from math import cos
from math import sqrt

def RK4(f, h, y, t):
    h2 = h/2
    k1 = f(t, y)
    k2 = f(t + h2, y + h2 * k1)
    k3 = f(t + h2, y + h2 * k2)
    k4 = f(t + h, y + h * k3)

    return y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.

def f(t, y):
    return t + cos(y / sqrt(5))

y0, t0, h, tmax = 2.6, 1.8, 0.1, 2.9
y, t = y0, t0
while t <= tmax:
    print("t = " + str(t) + "   " + "y = " + str(y))
    y = RK4(f, h, y, t)
    t += h
