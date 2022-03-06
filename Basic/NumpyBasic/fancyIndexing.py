"""
팬시 색인
정수 배열을 사용한 색인을 설명하기 위해 Numpy 에서 차용한 단어
슬라이싱과는 달리 선택된 데이터를 새로운 배열로 복사.
"""
import numpy as np
arr = np.empty((5,4))
for i in range(5):
    arr[i] = i
print(arr)

# 특정한 순서로 로우를 선택하고 싶다면 그냥 원하는 순서가
# 명시된 정수가 담긴 ndarray or list 를 주면 됨.
print(arr[[4,3,0,2]])

print(arr[[-1,-2,-3]]) # 음수를 통해 역순

arr2d = np.arange(32).reshape((8, 4))
print(arr2d)
print(arr2d[[1,5,7,2], [0,3,1,2]]) # [ 4 23 29 10] 4: arr[1][0] 23: arr[5][3] ...
print(arr2d[[1, 5, 7, 2]][:, [0, 3, 1, 2]]) # 1 행에서 0,3,1,2 data 5행 에서 0,3,1,2 data...
"""
[[ 4  7  5  6]
 [20 23 21 22]
 [28 31 29 30]
 [ 8 11  9 10]]
"""
CopyOfArr = arr[[4,3,0,2]]
CopyOfArr[1] = 7
print(CopyOfArr)
print(arr)

