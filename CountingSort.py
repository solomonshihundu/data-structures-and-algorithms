def counting_sort(arr,n):
   
    # get the largest value in
    # the array
    max_val = max(arr)

    # declare output array, initialized to the size
    # of the highest value in the array
    output = [0]*(max_val+1)

    # loop through input arrays
    for i in range(n):
        # if number occuers increase the index of output array
        # by one
        if arr[i] >= 0 and arr[i] < 100:
            if output[arr[i]] > 0:
                output[arr[i]] += 1
            else:
                output[arr[i]] = 1
            
    print(output)

arr = [1,1,3,2,1]
n = len(arr)
counting_sort(arr,n)