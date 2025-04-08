import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array)

array = np.delete(array, 0, axis=0)
print()
print(array)

# array = np.insert(array, 0, [11, 12, 13], axis=0)
# print()
# print(array)

# array = np.append(array, [[44, 55, 66]], axis=0)
# print()
# print(array)