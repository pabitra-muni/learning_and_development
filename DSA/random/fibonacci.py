#print the nth value in fibonacci series

def fibonacci(n: int):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

position = int(input())
print(fibonacci(position))
