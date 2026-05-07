# Print 1D array with 5 zeros.

import numpy as np

num = np.zeros(5)
num2 = np.zeros((2,3))
num3 = np.zeros(((2,3,3)))

print("1-D array",num)
print("2-D array",num2)
print("3-D array",num3)


identity_matrix = np.eye(4)
print(identity_matrix)