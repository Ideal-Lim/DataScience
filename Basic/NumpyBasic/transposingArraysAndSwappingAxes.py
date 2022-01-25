"""
배열 전치 (Transposing Arrays)
데이터를 복사하지 않고 데이터의 모양이 바뀐 뷰를 반환하는 특별한 기능이다.
ndarray 는 transpose 메서드와 T라는 이름의 특수한 속성을 가지고 있다.
T 속성을 이용하는 간단한 전치는 축을 뒤바꾸는 경우다.
"""
import numpy as np
arr = np.arange(15).reshape((3, 5))
print(arr) # (3,5)
print(arr.T) # (5,3)

# np.dot 을 이용한 행렬의 내적 구하기
arr = np.random.randn(6, 3)
print(arr)
print(np.dot(arr.T, arr))

#
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print(arr.transpose((1, 0, 2)))

"""
ndarray 에는 swapaxes 라는 메서드가 있는데 두개의 축 번호를 받아서 배열을 뒤바꾼다.  
"""
print(arr.swapaxes(1,2))
