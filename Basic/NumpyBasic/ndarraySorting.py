import numpy as np
arr = np.random.randn(6)
print(arr)
arr.sort() # 기존 배열을 정렬
print(arr)

arr = np.random.randn(5,3)
arr2 = arr.copy()
print(arr)
arr.sort() # row sorting
print(arr)

print(arr2)
arr2.sort(0) # column sorting
print(arr2)

# np.sort : 배열을 직접 변경하지 않고 정렬된 결과를 가지고 있는 새 배열 반환
arr = np.random.randn(5,3)
print(arr)
print(np.sort(arr))
print(arr)
