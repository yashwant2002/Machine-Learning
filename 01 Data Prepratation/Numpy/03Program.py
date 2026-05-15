# Create a NumPy array from 1 to 10 and find:
# arrange : for range creation
# shape : structure of array
# data type
# sum
# mean

import numpy as np

arr = np.arange(1,11)

print("Array: ",arr)
print("Array: ",arr.shape)
print("Array: ",arr.dtype)
print("Array: ",np.mean(arr))
print("Array: ",np.sum(arr))