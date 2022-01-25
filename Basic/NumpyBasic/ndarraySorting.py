import numpy as np
arr = np.random.randn(6)
print(arr)
arr.sort() # 기존 배열을 정렬
print(arr)

arr = np.random.randn(5,3)
print(arr)
arr.sort() # row sorting
print(arr)

arr = np.random.randn(5,3)
print(arr)
arr.sort(0) # column sorting
print(arr)

# np.sort : 배열을 직접 변경하지 않고 정렬된 결과를 가지고 있는 새 배열 반환
arr = np.random.randn(5,3)
print(arr)
np.sort(arr)
print(arr)
