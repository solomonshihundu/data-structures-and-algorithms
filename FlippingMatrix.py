def fliping_matrix(matrix,n):
    
    n = n // 2
    arr = []
    for i in range(n):
        for j in range(n):
            temp = []
            #print(matrix[i][j],"")
            temp.append(matrix[i][j])

            #print(matrix[i][2*n-j-1])
            temp.append(matrix[i][2*n-j-1])

            #print(matrix[2*n-i-1][j])
            temp.append(matrix[2*n-i-1][j])

            #print(matrix[2*n-i-1][2*n-j-1])
            temp.append(matrix[2*n-i-1][2*n-j-1])

            print(temp)

            arr.append(max(temp))
    return sum(arr)
            

matrix = [[112,42,83,119],
          [56,125,56,49],
          [15,78,101,43],
          [62,98,114,108]]

n = len(matrix)
print(fliping_matrix(matrix,n))