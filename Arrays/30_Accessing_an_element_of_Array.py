import array

arr1 = array.array("i", [1, 2, 3, 4, 5, 6])


def accessElement(array, index):
    if index >= len(array):
        print("There is not an element in this index")
    else:
        print(array[index])


accessElement(arr1, 0)
accessElement(arr1, 6)
accessElement(arr1, 10)
