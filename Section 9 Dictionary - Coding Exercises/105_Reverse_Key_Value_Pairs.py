# Reverse Key-Value Pairs
# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

# Example:

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# reverse_dict(my_dict)
# Output:

# {1: 'a', 2: 'b', 3: 'c'}


def reverse_dict(my_dict):
    newDict = {value: key for key, value in my_dict.items()}
    return newDict
