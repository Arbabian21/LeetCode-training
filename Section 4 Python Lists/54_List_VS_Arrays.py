# Similarities betwen lists and ararys in python
## Both data structures are mutable (able to be changed)
## Both can be indexed and iterated through
## They can both be sliced

# Differences
## Arrays are better for arithmetic operations (doing math on them)

import numpy as np

myArray = np.array([1,2,3,4,5])
myList = [1,2,3,4,5]

print(myArray/2) # Divides each element in array by 2

try:
	print(myList/2)
except :
	print('You cannot do arithmetic on lists')

## Arrays, all elements need to be the same data type
## Lists, all elements can be different
myArray = np.array([1,2,3,4,5,'string']) ### This converts everything from ints into strings
myList = [1,2,3,4,5, 'string'] ### Everything remains it's original data type
print(myArray)
print(myList)

## Functions on arrays return a new array and do not change the original one
## Functions on lists do not return a new list and DO change the original list
newArray = np.append(myArray,[11])
myList.append(11)

print(myArray)
print(newArray)
print(myList)