myDict = {"name": "Eddie", "age": 26, "address": "London"}
print(myDict)
# Time and Space O(1)
del myDict["age"]
print(myDict)

# Time and Space  O(1)
removed_element = myDict.pop("address", None)
print(removed_element)
print(myDict)


anotherRemovedElement = myDict.popitem()
print(anotherRemovedElement)
print(myDict)


# Time O(n) space O(1)
myDict = {"name": "Eddie", "age": 26, "address": "London"}
print(myDict)
myDict.clear()
print(myDict)