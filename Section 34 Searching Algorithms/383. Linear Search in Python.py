def linearSearch(input, target): # time complex O(n) space complex O(1)
    for i in range(len(input)):
        if input[i] == target:
            return i
    return -1