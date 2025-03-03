#print the nth value in fibonacci series

"""
time complexity = O(n)
space complexity = O(n) for recusive stack 
"""
def fibonacci(n: int):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# time complexity of O(n) with no additional space complexity
def fibonacciOptimized(n: int):
    if n==1 or n==2:
        return 1
    prev2 = 1
    prev = 1
    print(prev2, end=" ")
    print(prev, end=" ")
    for i in range(3, n + 1):
        cur = prev + prev2
        prev2 = prev
        prev = cur
        print(cur, end=" ")

fibonacciOptimized(10)
