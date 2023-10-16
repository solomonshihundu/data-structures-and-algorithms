def permute(arr):
    # No permutation on an empty list
    if len(arr) == 0:
        return []
    # Return element if its the only element 
    if len(arr) == 1:
        return arr

    # store all permutations
    l = []

    # looping through the a list, capture the first element
    # in the array with every loop
    # Consider Iteration 1 : 
    # i = 0

    for i in range(len(arr)):
        # m = 1
        m = arr[i] 
        print("Itr : ",i)
        print(m)
        
        # capture the sub-array excuding the element in the
        # current iteration [m] 
        # remList = [2,3]
        remList = arr[:i] + arr[i+1:] 

        # recursively call the permute method with the sub-arry
        # as input, looping through the results of permutaion
        for p in permute(remList):
            # Ensuring the output generated is a list
            # append the result of each cycle to 'm' then
            # store the result in a final output list
            if type(p) == list:
                l.append([m] + p)
            else:
                ls = list(map(int, str(p)))
                l.append([m] + ls)
    return l

arr = [1,2,3]
for p in permute(arr):
    print(p)