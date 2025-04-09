# Update / add an element into the dicitonary

myDict = {"name": "Eddie", "age": 26}
print(myDict)
# Time O(n) Space O(n)
myDict["age"] = 21
print(myDict)
myDict["name"] = "Arbab"
print(myDict)

# it updates if it already existss
# if it does not exist, it adds it

# Time and Space O(1)
myDict["address"] = "Richmond"
print(myDict)
