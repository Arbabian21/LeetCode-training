# Here's how to make a copy of a list
prevList = [1,2,3,4]
newList = []
print(prevList)
print(newList)

for i in prevList:
    doubledValue = i*2
    newList.append(doubledValue)
    
print(prevList)
print(newList)

# Here's the list comprehension way to do it
secondNewList = [i*2 for i in newList]
print(secondNewList)

# Another example of list comprehension
name = 'Arbabian'
nameList = [i for i in name]
print(name)
print(nameList)

# Comprehension also workes on other data structures
## Lists
## Range
## String
## Tuples