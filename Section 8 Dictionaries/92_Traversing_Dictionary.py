myDict = {"name": "Eddie", "age": 26, "address": "London"}

# Time O(n) Space O(1)
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)