def fibonacci(n):

    # Write your code here.
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)

n = int(input())
print(fibonacci(n))
