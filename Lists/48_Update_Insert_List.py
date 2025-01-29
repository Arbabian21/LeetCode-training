myList = [1,2,3,4,5]
print(myList)

# Update element
myList[2] = 33
print(myList)
    # Time and Space O(1)

# Insert
myList.insert(0,11)
print(myList)
    # Time and Space O(n)

# Append
myList.append(55)
print(myList)
    # Time and Space O(1)

# Extend
newList = [11,12,13,14] # This being n
myList.extend(newList)
print(myList)
    # Time and Space O(n)