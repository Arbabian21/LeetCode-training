a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Concatenate lists together using + operator
c = a + b
print(c)

# Print multiple times
print(c*2)

# len function
## returns the count of elements in the list
print(len(a))

# Max function
## returns the item witht the highest value in the list
print(max(b))

# Min function
## returns the item with the lowest value in the list
print(min(b))

# Sum function
## Returns the sum of all the items in the list
print(sum(c))

### so to get the average of a list
print(sum(c)/len(c))

# Convert the following code to use the list functions we learned
# total = 0
# count = 0
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#     average = total/count
# print('Average:', average)

myList = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    myList.append(value)
    average = sum(myList)/len(myList)
        
print('Average:', average)