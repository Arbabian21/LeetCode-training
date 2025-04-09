myDict = {"name": "Eddie", "age": 26, "address": "London"}

# Time O(n) Space O(1)
def searchDict(inputDict, target):
    for key in inputDict:
        if inputDict[key] == target:
            return key, target
    return "Not in dictionary"

print(searchDict(myDict, 26))
print(searchDict(myDict, 27))
