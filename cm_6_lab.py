
from math import sqrt
from math import sin

#rectangle method
def calculate_dx (a, b, n):
	return (b-a)/float(n)

def rect_rule (f, a, b, n):
	total = 0.0
	dx = calculate_dx(a, b, n)
	for k in range (0, n):
        	total = total + f((a + (k*dx)))
	return dx*total

def rect_rule_left (f, a, b, n):
	total = 0.0
	dx = calculate_dx(a, b, n)
	for k in range (0, n):
        	total = total + f((b - (k*dx)))
	return dx*total

def f(x):
    return sqrt(x) * sin((3.14 * x) / 3.0)**2



print (rect_rule(f, 0, 3, 1000))
print (rect_rule_left(f, 0, 3, 1000))




#trapezoid method
#!/usr/bin/env python
#from __future__ import division

def trapezoidal_rule(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite trapezoidal rule, using n subintervals"""
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    return s * h / 2

print (trapezoidal_rule(f, 0.0, 3.0, 1000))
# displays 1000000000.75

