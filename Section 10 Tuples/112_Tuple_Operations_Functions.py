myTuple = (1,2,4,3,2,5)
otherTuple = (1,2,6,9,8,7)

print(myTuple + otherTuple)
print()

print(myTuple*3)
print()

print(5 in myTuple)
print(12 in myTuple)
print()

print(myTuple.count(2))
print()

print(otherTuple.index(8))
print()

print(len(myTuple))
print()

print(max(myTuple))
print(min(myTuple))
print()

# tuple method is used to convert list into tuple
list1 = [1,2,3,4,5,'a']
tupleOfList = tuple(list1)
print(tupleOfList)