newTuple = ("a", "b", "c", "d", "e")
print(newTuple)
print(f"Index zero has {newTuple[0]}")
print(f"Index -1 has {newTuple[-1]}") # you can go in reverse order
print(newTuple[0:3]) # You can use the spread
print(newTuple[::-1])

# however you cannot use indexing to change elements 
# tuples are immutable
# CANNOT DO: newTuple[0] = 'f'