# numpy arrays
# efficient memory management and storage
#  faster reads and writes
#  it's an external package, we need to install and then import

import numpy as np

# collection object is used to create numpy arrays
arr = [1,2,3,4,5]

onedimarry = np.array(arr)
# print(onedimarry)
# print(type(onedimarry)) # type pf the object
# print(onedimarry.shape) # shape of the array | find the number of elements
# print(onedimarry.ndim) # number of dimensions
# print(onedimarry.size) # number of elements in the array



# create 2D array

arr2 = [[1,2,3],[4,5,6],[7,8,9]]
twodimarry = np.array(arr2)
# print(twodimarry)
# print(type(twodimarry)) # type pf the object
# print(twodimarry.shape) # shape of the array | find the number of elements     
# print(twodimarry.ndim) # number of dimensions
# print(twodimarry.size) # number of elements in the array
# print(twodimarry[0,0]) # access element at row 0 and column 0   


# airthmetic operations on arrays
#  +, -, *, /, \
# print(onedimarry * onedimarry) # element wise multiplication
# print(onedimarry + onedimarry) # element wise addition
# print(onedimarry - onedimarry) # element wise subtraction
# print(onedimarry / onedimarry) # element wise division


# print(twodimarry * twodimarry) # element wise multiplication
# print(twodimarry + twodimarry) # element wise addition
# print(twodimarry - twodimarry) # element wise subtraction
# print(twodimarry / twodimarry) # element wise division
# print(twodimarry @ twodimarry) # matrix multiplication
# print(np.dot(twodimarry, twodimarry)) # matrix multiplication using dot function
# print(np.matmul(twodimarry, twodimarry)) # matrix multiplication using matmul function
# print(np.multiply(twodimarry, twodimarry)) # element wise multiplication using multiply function
# print(np.add(twodimarry, twodimarry)) # element wise addition using add function
# print(np.subtract(twodimarry, twodimarry)) # element wise subtraction using subtract function
# print(np.divide(twodimarry, twodimarry)) # element wise division using divide function



#  concept of broadcasting
arr3 = [[1,2,3],[4,5,6],[7,8,9]]

# print(np.array(arr3) *3)


# changing dimensions of array
#  1d --> 2d 
#  2d --> 1d
#  connvert 2d to 1d using ravel() 

con1 = twodimarry.ravel()
# print(con1)

#  convert 1d array to 2d array using shape function
