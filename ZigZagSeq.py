# zigzag seq is such that the first k elements are in inc order
# and the last k elements are in dec order, where k = (n+1)/2
# lexicographically : 1,2,3 = 123,132,213,231,312,321 permutations
# sample [2,3,5,1,4] >> [1,4,5,3,2]
def findZigZagSequence(a, n):
    # sort the input array in ASC order
    # [1,2,3,4,5]
    a.sort()

    mid = int((n + 1)/2)            # k variable 
    a[mid], a[n-1] = a[n-1], a[mid] # [1,2,5,4,3]

    st = mid + 1                    # 4
    ed = n - 1                      # 4
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st] # [1,2,5,3,4] , 
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

arr = [2,3,5,1,4]
n = len(arr)
findZigZagSequence(arr,n)