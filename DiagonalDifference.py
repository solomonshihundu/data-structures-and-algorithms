# Using python regular expressions
def diagonal_difference(arr,n):
    x = abs(sum((arr[i][i]-arr[i][n-1-i]) for i in range(n)))
    print(x)

# using for loop and basic addidtion
def diagonal_diff(arr,n):

    # vars to store the sum of diagonals
    primary,secondary = 0,0

    # loop through the multidimesional arry
    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n-1-i]

    # result is the absolute difference of the sum of diagonals
    result = abs(primary - secondary)

    print(result)

    
        
arr_size = 3
arr = [[11,2,4],[4,5,6],[10,8,-12]]
diagonal_difference(arr,arr_size)
diagonal_diff(arr,arr_size)