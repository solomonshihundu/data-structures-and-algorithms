
# Using count function in python arrays
def lonely_integer(arr,n):
    # Ensure the array size if between  1 and 100
    if n >=1 and n <= 100:
        # Ensureing that the array size is an odd number
        if n % 2 == 1:
            # loop through the array
            for i in range(0, n):
                # ensuring the elements in array are
                # between the values of 0 and 100
                if arr[i] >= 0 and arr[i] <= 100:
                    # using array count methos, if count of the current 
                    # element in the array is 1
                    # return the current array
                    if arr.count(arr[i]) == 1:
                        return arr[i]

arr = [1,2,3,4,3,2,1]
n = len(arr)
result = lonely_integer(arr,n)
print(result)

#using a dictonary that stores each elements count
def lonely_int_dict(arr):
    # declare an empty dictionary
    count = {}
    # looping through the input dictionary
    for i in arr:
        # if the current ement is not already in
        # the dictionary, set its value as 1
        if i not in count:
            count[i] = 1
        # if the current element is already in
        # the dictionary, increase its value by 1
        else:
            count[i] += 1
    # return the key in the dictionary, whose
    # value is the least
    return list(count.keys())[list(count.values()).index(min(count.values()))]
    

result = lonely_int_dict(arr)
print(result)
