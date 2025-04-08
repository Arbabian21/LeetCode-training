import numpy as np

twoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Initial Two Dimensional Array:\n {twoDArray} \n\n')

new2Darray = np.insert(twoDArray, 0, [[0,0,0]], axis=0) # second param is index of row/col and axis param is what determines if
                                                        # it's going to be a row insertion or column insertion. 0 = row, 1 = col
print(f'Original Two Dimensional Array:\n {twoDArray} \n')
print(f'New Two Dimensional Array With insertion for Row at index 0:\n {new2Darray} \n\n')

anotherNew2Darray = np.insert(twoDArray, 1, [[1,1,1]], axis=1) # second param is index of row/col and axis param is what determines if
                                                        # it's going to be a row insertion or column insertion. 0 = row, 1 = col
print(f'Original Two Dimensional Array:\n {twoDArray} \n')
print(f'New Two Dimensional Array With insertion for Column at index 1:\n {anotherNew2Darray} \n\n')

appendtwoDArray = np.append(twoDArray, [[2,2,2]], axis=0)
print(f'Original Two Dimensional Array:\n {twoDArray} \n')
print(f'New Two Dimensional Array With append for row:\n {appendtwoDArray} \n\n')
