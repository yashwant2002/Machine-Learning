# how to create Array ?
import numpy as np

# 1-D Array
num= [1,2,3]
num = np.array(num)
print("1-D Array: ",num)

# 2-D array
num2 = [[1,2,3],[4,5,6]]
num2 = np.array(num2)
print("2-D Array: ",num2)

# 3-D Array
num3 = [[[1,2,3],[4,5,6],[7,8,9]]]
num3 = np.array(num3)
print("3-D Array: ",num3)

print("Datatype:",num3.dtype)