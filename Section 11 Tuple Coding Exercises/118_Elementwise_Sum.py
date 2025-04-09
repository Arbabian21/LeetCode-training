# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

# Example

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)

def tuple_elementwise_sum(tuple1, tuple2):
    returnTupleAsList = []
    for i in range(len(tuple2)):
        add = tuple1[i] + tuple2[i]
        returnTupleAsList.append(add)
        print(add)
    return tuple(returnTupleAsList)

def tuple_elementwise_sum(tuple1, tuple2):
    returnTuple = tuple(tuple1[i] + tuple2[i] for i in range(len(tuple1)) if len(tuple1) == len(tuple2))
    return tuple(returnTuple)
