# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

# my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict))
# Output:

# b

def max_value_key(my_dict):
    currMax = ''
    for letter, number in my_dict.items():
        if my_dict.get(currMax, -1) < number:
            currMax = letter
    return currMax
        
