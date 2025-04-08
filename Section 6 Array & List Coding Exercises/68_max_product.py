# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example

# arr = [1, 7, 3, 4, 9, 5] 
# max_product(arr) # Output: 63 (9*7)

def max_product(arr):
    firstLargest = 0
    secondLargest = 0

    
    for i in arr:
        if i > firstLargest:
            secondLargest = firstLargest
            firstLargest = i
        elif i > secondLargest:
            secondLargest = i
            
    return(firstLargest * secondLargest)
    
