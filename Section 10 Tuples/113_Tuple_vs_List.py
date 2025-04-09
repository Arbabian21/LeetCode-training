list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1)
list1[1] = 3  # you can change specific elements
print(list1)

list1 = [5, 4, 3, 2, 1]
print(list1)

list1 = [1, 2, 3, 4, 5, 6, 7]

# you can use del to delete elements
del list1[0]
print(list1)

# now if we try the same with tuples you will see we cannot
myTuple = (0, 1, 2, 3, 4, 5, 6, 7)
try:
    myTuple[0] = 12
except TypeError:
    print("you cannot reassign values in tuples")

# you can however reassign an entire tuple
myTuple = (1, 1, 1, 1, 11, 1)
print(myTuple)

try:
    del myTuple[1]
except:
    print("you cannot delete an element from a tuple")

print("you can however delete an entire tuple")
del myTuple

# you can use len(), min(), max(), sum(), any(), all(), and sorted() on both

# lists can be stored in typles and tuples can be stored in lists
list1 = [(1, 2), (3, 4), (5, 6)]
print(list1)
print(type(list1))
print(type(list1[0]))

tuple1 = ([1, 2, "1"], [2, "f", (1, 2)])
print(tuple1)
print(type(tuple1))
print(type(tuple1[1]))
print(type(tuple1[1][2]))

# nested tuple
nestedTuple = (
    (1, 2),
    (2, 3),
)

