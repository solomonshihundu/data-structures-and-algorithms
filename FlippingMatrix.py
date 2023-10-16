def fliping_matrix(matrix,n):
    # Solution

#     consider the below matrix
#         
#       [a,b]
#       [c,d]
#       
#       is our submatrix, aim is to get the highest sum of the n x n submatrix
#       no matter the number of times you flip it into a 2n x 2n matrix 
#        
#       [ 
#       [a,b,b,a]
#       [c,d,d,c]
#       [c,d,d,c]
#       [a,b,b,a]]
#       These are the only possible possitions of the elemnts in the larger matrx,
#       thus getting the highest value of each element (a,b,c,d) and summing them
#       we get our desired solution  
#
    
    # get the absolute size of the submatrix
    n = n // 2

    # list to store final maximum valued array (a,b,c,d)
    arr = []

    # Row iterator
    for i in range(n):
        # colunm iterator
        for j in range(n):
            # list to store the elements with
            # every cycle i.e [a,a,a,a] .... [d,d,d,d] 
            temp = []

            temp.append(matrix[i][j])
            temp.append(matrix[i][2*n-j-1])
            temp.append(matrix[2*n-i-1][j])
            temp.append(matrix[2*n-i-1][2*n-j-1])

            # get the maximum value in the array
            arr.append(max(temp))
            
    return sum(arr)

matrix = [[112,42,83,119],
          [56,125,56,49],
          [15,78,101,43],
          [62,98,114,108]]

n = len(matrix)
print(fliping_matrix(matrix,n))