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

print ("By Gauss method:")

task = [[2.0,1.0,1.0,1.0],
        [4.0,1.0,0.0,-2.0],
        [-2.0,2.0,1.0,7.0]]
print (task)


answer = myGauss(task)
print ("Answer:")
print(answer)
