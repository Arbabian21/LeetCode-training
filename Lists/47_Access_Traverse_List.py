shoppingList = ['milk','cheese','butter']
print('using index to print items for list')
print('Shopping list at index 0 is ' + shoppingList[0])
print('Shopping list at index 1 is ' + shoppingList[1])
print('Shopping list at index 2 is ' + shoppingList[2])
print('\n')

print('using in statement to print true or false if something is in list')
print('milk' in shoppingList) #returns true
print('bread' in shoppingList) # returns false
print('\n')

print('using for loop and in statement to print items from list')
for item in shoppingList:
    print(item)
print('\n')  

print('using for loop and in statement alongside range and len functions to access items from list while in loop')
for i in range(len(shoppingList)):
    shoppingList[i] =+ shoppingList
print('\n')
    