def sub_array(s,d,m,n):
    
    # count varibale to store number of
    # time condition has been satisfied
    count = 0
    
    # loop through array, adding two contiguos 
    # elements, if the sum is equal b-day
    # increase count until we reach end of array
    # m = 3
    # d = 9
    # [2,1,3,5,1]
    # [2,1,3]=6
    # [1,3,5]=9
    # [3,5,1]=9

    # loop though input array
    # get the subarray equal to the month- size
    # sum the values of the subarray
    # if the value is equal to b-day, increase count by 1
    # return count
    for i in range(n):
        arr = s[i:i+m]
        if sum(arr) == d:
            count += 1
    return count
       
         

arr = [2,1,3,5,1]
d = 9
m = 3
n = len(arr)

# arr = [4]
# d = 4
# m = 1
# n = len(arr)

print(sub_array(arr,d,m,n))