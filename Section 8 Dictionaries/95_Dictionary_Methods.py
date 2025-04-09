myDict = {"name": "Eddie", "age": 26, "address": "London", "education": "masters"}
print(myDict)

myDict.clear()
print(myDict)

# Copy, returns shallow copy
myDict = {"name": "Eddie", "age": 26, "address": "London", "education": "masters"}
newDict = myDict.copy()
print(myDict)
print(newDict)

#  fromkeys(the keys, the value)
newDict2 = {}.fromkeys([1, 2, 3], 1)
print(newDict2)

# get(key, value: optional default value)
print(myDict.get("name"))
print(myDict.get("aslkdkfjadlkjk"))
print(myDict.get("aslkdkfjadlkjk", "nothing"))

# Items - returns a list of tuple pairs of the dictionary
print(myDict.items())

# keys- returns list of keys in dictionary
print(myDict.keys())

# popitem returns and removees element frm dict
print(myDict)
print(myDict.popitem())
print(myDict)

# setDefault add key with default value if it's not already in there. otherwise keep the exisitng value
myDict.setdefault("name", "Arbabian")  # name already exists so no addition
print(myDict)

myDict.setdefault(
    "occupation", "seeking employment"
)  # occupation does not exist so the key is made w the default value of seeking
print(myDict)

# pop returns and remvoes item or None if not exist
print(myDict.pop("nothing", None))
print(myDict.pop("occupation"))
print(myDict)

# values returns list of values in dict. kiond of like keys method
print(myDict.values())

# update - updates elements in a list to those from another dictionary or a list of tuples, overwriting any already in og list and inserting new ones not alraedy in it
updateDict = {"a": 1, "b": 2, "c": 3}
myDict.update(updateDict)
print(myDict)
updateDict = {"a": 2, "b": 4, "c": 6}
myDict.update(updateDict)
print(myDict)

