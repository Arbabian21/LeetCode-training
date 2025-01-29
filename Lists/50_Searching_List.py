myList = [10,20,30,40,50,60,70,80,90]

# The in operator
## Time complexity is O(n) because it does a linear search
target = 50
if target in myList:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")
    
# Implementing our own linear serach
## Time complex O(n)
def linearSearch(inputList, inputTarget):
    for i, value in enumerate(inputList):
        if value == inputTarget:
            return i
    return -1

print(linearSearch(myList, 10))
print(linearSearch(myList, 100))

## He kinda did it weird with the whole enumerate thing. So here's how I would do it to make it easier.
def myLinearSearch( inputList, inputTarget):
    for i in range(len(inputList)):
        if inputTarget == inputList[i]:
            return i
    return -1
        
print(myLinearSearch(myList, 40))
print(myLinearSearch(myList, 400))

