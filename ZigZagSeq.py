# zigzag seq is such that the first k elements are in inc order
# and the last k elements are in dec order, where k = (n+1)/2
# lexicographically : 1,2,3 = 123,132,213,231,312,321 permutations
# sample [2,3,5,1,4] >> [1,4,5,3,2]
def findZigZagSequence(a, n):
    print("Original : ",a)
    # sort the input array in ASC order
    # [1,2,3,4,5]
    a.sort()
    print("Sorted : ",a)
    mid = int((n - 1)/2)            # k variable 
    a[mid], a[n-1] = a[n-1], a[mid] # [1,2,5,4,3]

    print("Swaped  0 : ",a)

    st = mid + 1                    # 4
    ed = n - 2                     # 4
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st] # [1,2,5,3,4] , 
        st = st + 1
        ed = ed - 1
        print(a)

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

#arr = [2,3,5,1,4]
# arr = [1 ,2, 3 ,4, 5,6 ,7]
arr = [1 ,2, 3 ,4, 5,6 ,7,8,9]
n = len(arr)
findZigZagSequence(arr,n)