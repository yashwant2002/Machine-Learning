import numpy as np

arr = np.arange(1,21)
even_arr= arr[arr%2==0]
print(even_arr)