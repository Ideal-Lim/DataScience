"""
수학 메서드와 통계 메서드
배열 전체 혹은 배열에서 한 축을 따르는 자료에 대한 통계를 계산하는 수학 함수는 배열 메서드로 사용할 수 있다.
전체의 합이나 평균, 표준편차는 Numpy 의 최상위 함수를 이용하거나 배열의 인스턴스 메서드를 사용해서 구할 수 있다.
"""

import numpy as np
arr = np.random.randn(5, 4)
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())

# mean , sum : 선택적으로 axis 인자를 받아서 해당 axis에 대한 통계를 계산하고 한 차수 낮은 배열을 반환한다.
arr = np.arange(12).reshape(3,4)
print(arr)
print(arr.mean(axis = 1)) # row mean
print(arr.mean(axis = 0)) # column mean
print(arr.sum(axis = 1)) # row sum
print(arr.sum(axis = 0)) # column sum

#cumsum, cumprod : 각 원소의 누적합 / 누적곱 , 중간 계산값을 담고 있는 배열을 반환한다.
arr = np.arange(6)
print(arr)
print(arr.cumsum())
print(arr.cumprod())

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr.cumsum(axis = 0)) # column sum
print(arr.cumsum(axis = 1)) # row sum

print(arr.cumprod(axis = 0))
print(arr.cumprod(axis = 1))

# std, var : 표준편차와 분산, 선택적으로 자유도를 줄 수 있으며 분모의 기본값은 n이다

# min, max : 최솟값과 최댓값
print(arr.min())
print(arr.max())

"""
y = f(x) 라고 할 때
max는 y가 최대인 값, argmax는 y를 최대가 되도록 하는 x
min은 y가 최소인 값, argmin은 y를 최소가 되도록 하는 x 
"""
# argmin, argmax : 최소 원소의 색인값과 최대 원소의 색인값
arr = np.random.randn(5, 4)
print(arr)
print(arr.argmin())
print(arr.argmax())
