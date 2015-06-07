from math import fabs
import py
import scipy.linalg

def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""

    # Converts N into a list of tuples of columns                                                                                                                                                                                                      
    tuple_N = zip(*N)

    # Nested list comprehension to calculate matrix multiplication                                                                                                                                                                                     
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def pivot_matrix(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)

    # Create an identity matrix, with floating point values                                                                                                                                                                                            
    id_mat = [[float(i ==j) for i in range(m)] for j in range(m)]

    # Rearrange the identity matrix such that the largest element of                                                                                                                                                                                   
    # each column of M is placed on the diagonal of of M                                                                                                                                                                                               
    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            # Swap the rows                                                                                                                                                                                                                            
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat

def lu_decomposition(A):
    """Performs an LU Decomposition of A (which must be square)                                                                                                                                                                                        
    into PA = LU. The function returns P, L and U."""
    n = len(A)

    # Create zero matrices for L and U                                                                                                                                                                                                                 
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    # Create the pivot matrix P and the multipled matrix PA                                                                                                                                                                                            
    P = pivot_matrix(A)
    PA = mult_matrix(P, A)

    # Perform the LU Decomposition                                                                                                                                                                                                                     
    for j in range(n):
        # All diagonal entries of L are set to unity                                                                                                                                                                                                   
        L[j][j] = 1.0

        # LaTeX: u_{ij} = a_{ij} - \sum_{k=1}^{i-1} u_{kj} l_{ik}                                                                                                                                                                                      
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1

        # LaTeX: l_{ij} = \frac{1}{u_{jj}} (a_{ij} - \sum_{k=1}^{j-1} u_{kj} l_{ik} )                                                                                                                                                                  
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]

    return (P, L, U)

def lu (A, A_size, result):
    det = 1e0 
    for j in range(1, A_size + 1):
        for i in range(1, j):
            sum = A[i][j]
            for k in range(1, i): sum -= A[i][k] * A[k][j]
            A[i][j] = sum

        amax = 0e0
        for i in range(j, A_size + 1):
            sum = A[i][j]
            for k in range(1, j): sum -= A[i][k] * A[k][j]
            A[i][j] = sum

            if amax < fabs(A[i][j]) : amax = fabs(A[i][j]); imax = i

            if amax == 0e0 : print ("Singular matrix!"); return 0e0

            result[j] = imax

            if imax != j:
                det = -det
                for k in range(1, A_size + 1):
                    t = A[imax][k]; A[imax][k] = A[j][k]; A[j][k] = t

            det *= A[j][j]
            t = 1e0 / A[j][j]

            for i in range(j + 1, A_size + 1): A[i][j] *= t
    return det

def LUsystem (A, ipivot, B, n):
    for i in range(1, n + 1):
        sum = B[ipivot[i]]
        B[ipivot[i]] = B[i]
        for j in range(j, i): sum -= A[i][j] * B[j]
        B[i] = sum

    for i in range(n, 0, -1):
        sum = B[i]
        for j in range(i + 1, n + 1): sum -= A[i][j] * B[j]
        B[i] = sum / A[i][j]

def myGauss(m):
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
        print (m)
    ans = []
    m.reverse() 
    result = 0.0
    for sol in range(len(m)):
            if sol == 0:
                result = m[sol][-1] / m[sol][-2]
                ans.append(result)
                print (str(sol) + ' ' + str(result))
            else:
               
                inner = 0
                for x in range(sol):
                    inner += (ans[x]*m[sol][-2-x])
                result = (m[sol][-1]-inner)/m[sol][-sol-2]
                ans.append(result)
                print (str(sol) + ' ' +str(result))
    ans.reverse()
    return ans
        
ipivot = [0, 0, 0]
A = [[2.0, 1.0, 1.0],
    [4.0, 1.0, 0.0],
    [-2.0, 2.0, 1.0]]

B = [1.0, -2.0, 7.0]

P, L, U = lu_decomposition(A)
print(L)
print(U)
for i in range(len(L)):
    L[i].append(B[i])

Y = myGauss((L))
print (Y)
for i in range(len(U)):
    U[i].append(Y[i])

answer = myGauss(U)
print (answer)

