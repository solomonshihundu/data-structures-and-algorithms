def permute(arr):
    # No permutation on an empty list
    if len(arr) == 0:
        return []
    # Return element if its the only element 
    if len(arr) == 1:
        return arr

    # store all permutations
    l = []

    for i in range(len(arr)):
        m = arr[i] 
        
        # First Itr, [2, 3]
        # Sec Itr, [3]
        # print("Itr : ",i)
        remList = arr[:i] + arr[i+1:] 
        # print(remList)

        for p in permute(remList):
            print(p)
            l.append([m] + p)
    return l

arr = [1,2,3]
for p in permute(arr):
    print(p)