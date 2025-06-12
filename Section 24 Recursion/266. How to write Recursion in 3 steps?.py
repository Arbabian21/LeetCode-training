def factorial(n): # time complex O(n) space complex O(n)
    if n <= 1 or not int(n) == n: # remember to think of possibly breaking inputs
        # n == 1 would only work if the input is non-negative factorial(-10)
        # n <= 1 would only work for whole number inputs facrotial(10.2)
        return 1
    return n * factorial(n-1)

print(factorial(1.5))