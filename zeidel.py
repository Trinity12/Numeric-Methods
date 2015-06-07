from math import fabs

def convenge(a, b, eps): #умова завершення
    error = 0
    for i in range(len(a)):
        error += fabs(a[i] - b[i])

    if error < eps: return False
    else: return True

def seidel(A, B, eps):
    previous = []
    current = []
    for i in range(len(A)): previous.append(0); current.append(0)
    while convenge(current,previous,eps):
        for i in range(len(A)):
            var = 0
            for j in range(len(A)):
                if j != i: var += A[i][j] * current[j]

            previous[i] = current[i]
            current[i] = (B[i] - var) / A[i][i]
        


ipivot = [0, 0, 0]
A = [[2.0, 1.0, 1.0],
    [4.0, 1.0, 0.0],
    [-2.0, 2.0, 1.0]]

B = [1.0, -2.0, 7.0]

print ("input eps: ")
eps = input()

print (seidel(A, B, float(eps)))