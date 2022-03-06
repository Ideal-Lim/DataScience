import numpy as np
# Generate some random data
data = np.random.randn(2, 3)
print(data)
# 행렬 곱
print(data*10)
# 행렬 합
print(data + data)
# data 행렬 크기
print(data.shape)
# data 타입
print(data.dtype)

"""s
ndarray 생성
"""
data1 = [1,2,3,4,5]
data2 = [[1,2,3,4], [5,6,7,8]]
# list -> ndarray
arr1 = np.array(data1)
arr2 = np.array(data2)
print(type(arr1))
# ndim : 차원
print(arr2.ndim)

# 0 행렬 생성
print(np.zeros(10))
print(np.zeros((3, 6)))
# 메모리를 초기화 하지 않기 때문에 예상하지 못한 쓰레기 값이 들어가 있음.
print(np.empty((2, 3, 2)))
# 1 행렬 생성
print(np.ones((2,3)))

#something_like : _like는 지정된 array의 shape 크기만큼 지정된 값으로 채워 array 를 반환한다.
np.ones_like(arr2)

print(np.arange(15)) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(np.arange(15).reshape(3, 5))

print(np.full((2,3), 5))

print(np.identity(3))
print(np.eye(3, k=1))
print(np.eye(3, k=-1))











