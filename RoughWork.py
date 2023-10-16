def rough_work():
    a = -10
    b = -100

    print(a)
    print("Hello")

    if -10 <= -100:
        print('-10 less than -100')
    else:
        print('-10 more than -100')

# rough_work()

def sub_array(arr):
    print(arr[:0]) # []
    print(arr[:1]) # [1]
    print(arr[:2]) # [1,2]
    print(arr[2:]) # [3]
    print(arr[3:]) # []
    print(arr[1:]) # [2,3]
    print(arr[0:]) # [1,2,3]
arr = [1,2,3]
sub_array(arr)