import array

my_array1 = array.array("i", [1, 2, 3, 4])


def linearSearch(array, searchParam):
    for i in range(len(array)):
        if array[i] == searchParam:
            return i
    return -1


print(linearSearch(my_array1, 3))
