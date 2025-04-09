newTuple = 'a', 'b', 'c', 'd', 'e'
print(newTuple)
print(type(newTuple))

# better way to write tuple
newTuple = ('a', 'b', 'c', 'd', 'e')
print(newTuple)
print(type(newTuple))

# single element tuples must end in a comma otherwise mistaken for whatever the type of the element is
newTuple = ('a',)
print(newTuple)
print(type(newTuple))

notATuple = ('a') # just a string in parenthesis
print(notATuple)
print(type(notATuple))

# built in tuple function
newTuple = tuple()
print(newTuple)
print(type(newTuple))

# but if you use this function it turns everything into it into a tuple
newTuple = tuple('123554')
print(newTuple)
print(type(newTuple))

# Time complexity O(1) Space complexity O(n)