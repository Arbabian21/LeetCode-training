# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

# Example:

# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# check_same_frequency(list1, list2)
# Output:

# False

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

def check_same_frequency(list1, list2):
    dict1 = {}
    for item in list1:
        dict1[item] = dict1.get(item, 0) + 1
        
    dict2 = {}
    for item in list2:
        dict2[item] = dict2.get(item, 0) + 1
        
    for key, value in dict1.items():
        if dict2[key] != value:
            return False 
    
    return True
    
print(check_same_frequency(list1,list2))