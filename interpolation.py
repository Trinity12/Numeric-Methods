from math import *
from numpy import *
from matplotlib import pyplot

def Fi(i, xi, x):
    res = 1
    for j in range(0, n):
        if j != i:
            res *= xi - x[j]
            res /= x[i] - x[j]
    return res

def Ln(xi, n, x, y):
    res = 0
    for i in range(0, n):
        res += y[i] * Fi(i, xi, x)
    return res


x = [1.415,   1.420,   1.425,   1.430,   1.435,   1.440,   1.445,   1.450,   1.455,   1.460]
y = [0.88 ,  0.889 ,  0.890 ,  0.891 ,  0.892 ,  0.893 ,  0.894 ,  0.895 ,  0.896,   0.897]
n = len(x)

xs, ys, ys_Newton = [], [], []
s = x[0]
y_Newton = y
#Y_counter(y_Newton)

while s <= x[n-1]:
    xs.append(s)
    s += 0.00005
for xi in xs:
    ys.append(Ln(xi, n, x, y))
   # ys_Newton.append(Interpolation_Newton(x, y_Newton, x[0], 1))

#ys_Newton = Newton(xs,y)

#pyplot.axis([x[0] - 1.0, x[n-1] + 1.0, y[0] - 1.0, y[n-1] + 1.0])
pyplot.plot (xs, ys, 'g', label = "Interpolated graph")
pyplot.plot (x, y, 'r.', label = "First graph")
pyplot.title("Intepolation Lagrange")
pyplot.show()
