import numpy as np

arr = np.arange(1, 11)

arr[arr % 2 != 0] = -1
arr[arr > 5] = 0

print(arr)
