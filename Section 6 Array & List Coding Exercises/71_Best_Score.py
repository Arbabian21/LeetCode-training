# Best Score
# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) # 90 87


def first_second(my_list):
    
    first = 0
    second = 0
    
    for i in my_list:
        if i > first:
            second = first
            first = i
        elif i > second:
            second = i
            
    return first, second
