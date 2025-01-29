# Add a condition to list comprehension

myList = [1,2,3,4,5,6,7,8,9,10]
newList = [i for i in myList if i % 2 == 0]

print(myList)
print(newList)

# Another example, square positive numbers
myList = [-1,2,-3,4,-5,6,-7,8,-9,10]
newList = [number*number for number in myList if number > 0]
print(myList)
print(newList)

# Another example, consanants
sentence = 'My name is Arbab'

def isConsanant(letter):
    vowels = ['a','e','i','o','u','y']
    return letter.isalpha() and letter.lower() not in vowels

consonants = [letter for letter in sentence if isConsanant(letter)]
print(sentence)
print(consonants)

# You can also put the condition on the beginning
myList = [-1,2,-3,4,-5,6,-7,8,-9,10]
newList = [number if number > 0 else 0 for number in myList]
print(newList)