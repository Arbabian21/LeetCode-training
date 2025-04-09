# Creating Dictionary
# Time O(1) Space O(1)
myDict = dict()
print(myDict)

myDict2 = {}
print(myDict2)

# Three different ways to make dictionaries 
# Time O(n) Space O(n)

# Creating using dict function
eng_spa = dict(one="uno", two="dos", three="tres")
print(eng_spa)

# Creating using curly braces
eng_sp2 = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_sp2)

# Creating a dictionary using tuples
eng_sp3_tuples = [("one", "uno"), ("two", "dos"), ("three", "tres")] 
eng_sp3 = dict(eng_sp3_tuples)
print(eng_sp3)