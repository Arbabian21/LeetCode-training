
myList = ['a','b','c','d','e','f']
print(myList)

# Slice
print(myList[0:3]) # start index (inclusive) : end index (exclusive)
print(myList[:2]) # No starting index, so beginning to just before index 2
print(myList[2:]) # No ending index, so from index 2 (inclusive) to the end
print(myList[:]) # Just the colon, prints everything

myList[0:3] = ['x','y','z']
print(myList)

# Deletion, Space complex for all Deletion methods is O(1)
## Pop
### If you use pop without param, Time 
### If you use pop with param, Time O(n) 

myList.pop(0) # Pops the index you give it, if you give it nothing then it'll pop from the end
print(myList)

print(myList.pop()) # Prints the thing you pop, meaning pop returns a value
print(myList)

## Delete
### Time Complex O(n)
del myList[1] # Deletes whatever is provided
print(myList)

del myList[0:2]
print(myList)

## Remove
### Time Complex O(n)
myList.remove('e')
print(myList)
