import array

my_array = array.array("i") # Empty array Time complexity is constance. 
                            # so is Space Complexity
print(my_array)

my_array1 = array.array("i", [1, 2, 3, 4]) # Time complexity to create an array of size 
                                           # is n
                                           # Space complexity is the same.
print(my_array1)
# Python default Array library can only handle primitive data types


import numpy as np

np_array = np.array([], dtype=int) # Constant Time and Space Complexity
print(np_array)

np_array1 = np.array([1,2,3,4]) # O(n) time and space complexity 
print(np_array1)