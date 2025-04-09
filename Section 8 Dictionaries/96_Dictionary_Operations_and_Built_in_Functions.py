myDict = {3: "three", 5: "five", 9: "nine", 2: "two", 1: "one", 4: "four"}

print("three" in myDict.values()) # true

print(len(myDict)) # 6

print(all(myDict)) # make sure ALL the keys are boolean true

print(any(myDict)) # make sure at least oney key are boolean true

print(sorted(myDict))