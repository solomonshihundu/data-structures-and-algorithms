def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)

n_terms = 10

if n_terms <= 0:
    print("Invalid Input! Please enter a value greater than 1")
else:
    print("Fibonacci Series of ",n_terms)
for i in range(n_terms):
    print(fib_recursive(i))

