def permute(arr):

    # store all permutations
    l = []

    # No permutation on an empty list
    if len(arr) == 0:
        return []
    # Return element if its the only element 
    if len(arr) == 1:
        return arr

    # looping through the a list, capture the first element
    # in the array with every loop

    for i in range(len(arr)):
        m = arr[i] 
        # capture the sub-array excuding the element in the
        # current iteration [m] 
        remList = arr[:i] + arr[i+1:] 
        # print(remList)

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
                print(l)
    return l

arr = [1,2,3]
for p in permute(arr):
    pass
    print(p)

############################################################################
#                               HOW IT WORKS                               #
############################################################################
#   Given the Array [1,2,3] 
# A)  In the first Main Iteration
#  i = 0, m = 1 , remList = [2,3]
#       Calling permute() recursively with remList as Input array, take (j) as iterator (i) in recursive call.
#       From l.append( m + p ) 
#       j = 0, m = 2 , remList = []+[3], p =  [3] = [2,3]
#       j = 1, m = 3 , remList = [2]+[], p =  [2] = [3,2] 
#       Calling l.append(m + p) recusively with m = 1
#       l = [[1,2,3],[1,3,2]]
# 
# B)  In the Second Main Iteration
#  i = 1, m = 2 , remList = [1,3]
#       Calling permute() recursively with remList as Input array, take (j) as iterator (i) in recursive call.
#       From l.append( m + p ) 
#       j = 0, m = 1 , remList = []+[3], p =  [3] = [1,3]
#       j = 1, m = 3 , remList = [1]+[], p =  [2] = [3,1] 
#       Calling l.append(m + p) recusively with m = 2
#       l = [[1,2,3],[1,3,2],[2,1,3],[2,3,1]]  
#
# C)  In the Third Main Iteration
#  i = 2, m = 3 , remList = [1,2]
#       Calling permute() recursively with remList as Input array, take (j) as iterator (i) in recursive call.
#       From l.append( m + p ) 
#       j = 0, m = 1 , remList = []+[2], p =  [3] = [1,2]
#       j = 1, m = 2 , remList = [1]+[], p =  [2] = [2,1] 
#       Calling l.append(m + p) recusively with m = 3
#       l = [[1,2,3],[1,3,2],[2,1,3],[2,3,1]2,[3,1,2],[3,2,1]]  
#
#
#
#
#
#
#