from math import *
from numpy import *
from matplotlib import pyplot

def Y_counter(Y_vect):
    Y_result = zeros((len(Y_vect),len(Y_vect)))
    for i in range(len(Y_vect)):
        Y_result[0][i] = Y_vect[i]

    i = 1
    j = 0
    while i < len(Y_vect):
        while j < n - i:
            Y_result[i][j] = Y_result[i-1][j+1] - Y_result[i-1][j]
            i += 1
            j += 1
    for i in range(len(Y_vect)):
        Y_vect[i] = Y_result[i][0]

    return Y_vect

def Interpolation_Newton(x, Y_vect, x0, step):
    q = (x - x0) / step
    result = Y_vect[0]

    mult_q = 1
    fact = 1

    i = 1
    while i < len(Y_vect):
        fact *= i
        mult_q *= (q - i + 1)
        result += mult_q / fact * Y_vect[i]

    return result

x = [1.415,   1.420,   1.425,   1.430,   1.435,   1.440,   1.445,   1.450,   1.455,   1.460]
y = [0.88 ,  0.889 ,  0.890 ,  0.891 ,  0.892 ,  0.893 ,  0.894 ,  0.895 ,  0.896,   0.897]
n = len(x)

xs, ys_Newton = [], []
s = x[0]
y_Newton = y
y_Newton = Y_counter(y_Newton)

while s <= x[n-1]:
    xs.append(s)
    s += 0.5
for xi in xs:
    #ys.append(Ln(xi, n, x, y))
    ys_Newton.append(Interpolation_Newton(x, y_Newton, x[0], 1))

#ys_Newton = Newton(xs,y)

#pyplot.axis([x[0] - 1.0, x[n-1] + 1.0, y[0] - 1.0, y[n-1] + 1.0])

pyplot.plot (xs, ys_Newton, label = "Interpolated graph")
pyplot.plot (x, y, 'r.', label = "First graph")
pyplot.title("Intepolation Newton")
pyplot.show()




