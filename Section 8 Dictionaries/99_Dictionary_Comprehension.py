# newDict = {newKey:newValue for item in list}
# newDict = {newKey:newValue for (key,value) in dict.items() if conditions}
import random

cityName = ["Paris", "London", "Rome", "Berlin", "Madrid"]
newDict = {city: random.randint(20, 30) for city in cityName}
print(newDict)

over25Dict = {city: temp for (city, temp) in newDict.items() if temp > 25}
print(over25Dict)
