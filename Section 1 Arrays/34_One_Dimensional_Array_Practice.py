import array

# Create array
print("Step 1")
customArray = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(customArray)

# Traverse array
print("\nStep 2")
for i in customArray:
    print(i)

# Access element in array
print("\nStep 3")
print(customArray[0])

# Append any valye to the arrray using append()
print("\nStep 4")
customArray.append(10)
print(customArray)

# Insert value into array using insert()
print("\nStep 5")
customArray.insert(0, 0)
print(customArray)

# Extend python array using extend()
# Allows you to add another array to the end of the selected array
print("\nStep 6")
customArray.extend([11, 12, 13, 14, 15, 16, 17, 18, 19])
print(customArray)

# Add items from list into array using fromlist()
print("\nStep 7")
customList = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
customArray.fromlist(customList)
print(customArray)

# Remove any array element using remove()
print("\nStep 8")
customArray.remove(0)
print(customArray)

# Remove last array element using pop()
print("\nStep 9")
customArray.pop()
print(customArray)

# Fetch any element through its index using index
print("\nStep 10")
x = customArray.index(10)
print(f"index for number 10 is {x}")
print(f"the value at index {x} is {customArray[x]}")

# Reverse a python array using reverse()
print("\nStep 11")
customArray.reverse()
print(customArray)

# Get array buffer information through buffer_info()
print("\nStep 12")
x = customArray.buffer_info()
print(f"Array buffer info is {x}")

# Check for number of occurances of an element using count()
print("\nStep 13")
x = customArray.count(2)
print(f"The number 2 occurs {x} times")

# Convert array to string using tostring()
# Append a string to char array using fromstring()
print("\nStep 14")
x = customArray.tobytes()
print(f"Our array as a bytes is {x}")
tempArray = array.array('i')
tempArray.frombytes(x)
print(f"Our array as back to normal is {tempArray}")

# Convert array to a python list with same elements using tolist()
print("\nStep 15")
x = customArray.tolist()
print(f"The array as a list is {x}")

# Slice elements from an array (basically substring)
print('\nStep 16')
print(f'A slice of our array is {customArray[1:10]}')