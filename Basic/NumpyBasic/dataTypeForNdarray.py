import numpy as np
arr1 = np.array([1,2,3], dtype = np.float64)
arr2 = np.array([1,2,3], dtype = np.int32)
print(arr1.dtype)
print(arr2.dtype)

arr = np.array([1,2,3,4,5])
print(arr)
print(arr.dtype) # int32
# astype : 형변환
float_arr = arr.astype(np.float64)
print(float_arr)
print(float_arr.dtype)

arr = np.array([2.6, 3.1, 5.2])
print(arr.astype(np.int32)) # [2 3 5]

# string -> float
numeric_strings = np.array(['1.24', '-2.4', '24'], dtype=np.string_)
print(numeric_strings.astype(float))# [ 1.24 -2.4  24.  ]

