import numpy as np
arr = np.arange(10)

arr_slice = arr[2:4]
arr_slice[:] = 16
print(arr)

# element indexing
print(arr[5]) # 5
# slicing
print(arr[5:8]) # [5 6 7]
arr[5:8] = 12 # [ 0  1  2  3  4 12 12 12  8  9]
# : is all elements
arr[:] = 0



arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2]) # [7 8 9]
print(arr2d[0][2]) # 3
print(arr2d[0, 2]) # 3
print(arr2d[:,1]) # [2 5 8]
print(arr2d[:2])
print(arr2d[:,:2])

arr2d_copy = arr2d.copy() # copy() : 새로운 ndarray 객체에 값을 복사.
arr2d_copy[0,0] = 1
print(arr2d)

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10,11,12]]])
print(arr3d[0]) # [[1, 2, 3], [4, 5, 6]]
print(arr3d[0][1]) # [4, 5, 6]
print(arr3d[0, 1]) # [4, 5, 6]
print(arr3d[:,1]) # [[ 4  5  6], [10 11 12]]



