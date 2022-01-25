"""
집합 관련 함수
Numpy 는 1차원 ndarray를 위한 몇가지 기본적인 집합 연산을 제공한다. 아마도 가장 자주 사용하는 함수는
배열 내에서 중복된 원소를 제거하고 남은 원소를 정렬된 형태로 반환하는 np.unique 일 것이다.
"""
import numpy as np
arr = np.array([1,2,3,4,3,2,1])
unique = np.unique(arr)
print(unique)

#sorted() 를 사용한 unique() 구현 -> List 반환
print(sorted(set(arr)))

# np.in1d : 두 개의 배열을 인자로 받아서 첫 번째 배열의 원소가 두 번째 배열의 원소를 포함하는 나타내는 불리언 배열을 반환
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6])) # [ True False False  True  True False  True]
