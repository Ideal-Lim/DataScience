"""
ufunc 유니버설 함수는 ndarray 안에 있는 데이터 원소별로 연산을 수행하는 함수다.
유니버설 함수는 하나 이상의 스칼라값을 받아서 하나 이상의 스칼라 결괏값을 반환하는
간단한 함수를 고속으로 수행할 수 있는 벡터화된 래퍼 함수라고 생각하면 된다.
"""
import numpy as np
"""
단항 유니버설 함수 : 인자 한개
"""
arr = np.arange(10)
# 제곱근
print(np.sqrt(arr))
# 지수
print(np.exp(arr))

"""
이항 유니버설 함수 : 인자 두개
"""
x = np.random.randn(8)
y = np.random.randn(8)

print(x, y)
# x, y 각 행렬마다 최댓값 출력
print(np.maximum(x, y))

arr = np.random.randn(7) * 5
print(arr)
# modf() : 분수를 받아서 몫과 나머지를 함께 반환한다.
remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)

print(arr)
print(np.sqrt(arr))
print(arr)
# 두 번째 인자로 arr 를 주면 arr에 계산결과를 저장한다.
print(np.sqrt(arr, arr))
print(arr)



