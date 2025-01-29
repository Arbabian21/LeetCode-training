# Turning a string into a list
a = 'spam'
b = list(a)
print(a)
print(b)

# Splitting a string by spaces
c = 'hello my name is arbab'
d = c.split()
print(c)
print(d)

# Splitting a string by a certain character
e = 'split_by_underscore'
f = e.split('_')
print(e)
print(f)

# Join (going from a list to a string)
g = "delimiter/is/forwardslash"
delimiter = '/'
h = g.split(delimiter)
print(g)
print(h)

## now to go backwards we use the delimiter and call the join function on it
i = delimiter.join(h)
print(i)