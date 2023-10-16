def factorial_recursive(n):
    if n == 1:
        return n
    else:
        # Method will call on itself until
        # the condition n == 1 is met
        # n x (n-1) x (n-2) x (n-3) x (n-4) x (n-5)
        # 6 x (5)   x (4)   x (3)   x (2)   x (1)
        return n * factorial_recursive(n-1)

num = 6

if num < 0:
    print("Invalid Input!")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of ",num," is ",factorial_recursive(num))


