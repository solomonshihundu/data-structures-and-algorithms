def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)

num = 6

if num < 0:
    print("Invalid Input!")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of ",num," is ",factorial_recursive(num))


