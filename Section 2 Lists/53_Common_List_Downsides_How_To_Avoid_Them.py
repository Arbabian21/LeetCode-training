myList = [2,4,3,1,5,7]
print(myList)

# List methods modify the argument and return null
myList.sort()
print(myList)

## The one above works but the one below will print null
myList = myList.sort()
print(myList)

myList = [2,4,3,1,5,7]
# If you try to use the append function, make sure to not pass the argument as a list
myList.append(10) #E DO THIS
print(myList)

myList.append([10]) ## DONT DO THIS
print(myList) ## It ends up being [2,4,3,1,5,6,[10]] because you  can add a list inside a list (nested list)
myList.pop()

# It's good practice to make a copy of the list you have before using a function on it, because the functions modify the original argument
copyList = myList[:] # make sure to use the spread operator ':' otherwise it'll just be a variable pointing to the memory location of 
                    # myList so when you change myList, it'll also show up in copyList
myList.sort()
print(copyList)
print(myList)