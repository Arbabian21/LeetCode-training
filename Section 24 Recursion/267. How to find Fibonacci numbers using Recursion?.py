def fibonacci(n): # time complex O(2^n)
    if n < 0 or not int(n) == n:
        return -1
    elif n in [0,1]:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(7.5))