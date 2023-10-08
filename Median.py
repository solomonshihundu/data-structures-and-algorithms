def find_median(arr,n):
    arr.sort()
    mid = n//2
    return arr[mid]

arr = [0,1,5,3,6,2,4]
n = len(arr)
print(find_median(arr,n))