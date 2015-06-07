from math import fabs

def isRight(A):
    sum_m = 0
    sum_diah = 0
    for i in range(len(A)):
        for j in range(len(A)):
            #if j != i: 
            sum_m += A[i][j]
            #else: sum_diah += A[i][j]
    #if not (fabs(sum_diah) > fabs(sum_m)): return False
    if fabs(sum_m) >= 1: return False
    else: return True

def Iteration(Ab, eps):
    size = len(Ab)
    previous = []
    current = []
    for i in range(size): previous.append(0); current.append(0)
    while (True):
        for i in range(size):
            current[i] = Ab[i][size]

            for j in range(size):
                if i != j: current[i] -= Ab[i][j] * previous[j]

            current[i] /= Ab[i][i]
        error = 0
        for i in range(size):
            error += fabs(current[i] - previous[i])

        if error < eps: break

        previous = current
        print(previous)
    return previous

 # розмірність матриці визначається по рядках

#ipivot = [0, 0, 0]

A = [[0.21, 0.12, -0.34, -0.16, -0.64],
    [0.34, -0.08, 0.17, -0.18, 1.42],
    [0.16, 0.34, 0.15, -0.31, -0.42],
    [0.12, -0.26, -0.08, 0.25, 0.83]]

if not isRight(A): print("can't"); input()
print ("input eps: ")
eps = input()

print (Iteration(A, float(eps)))

