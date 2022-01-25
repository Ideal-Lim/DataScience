"""
배열 연산으로 조건절 표현하기
numpy.where 함수는 x if 조건 else y 같은 삼항식의 벡터화된 버전이다. 다음과 같은 불리언
배열 하나와 값이 들어 있는 두 개의 배열이 있다고 하자.
"""
import numpy as np
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# cond 의 값이 True 일 때는 xarr의 값을 취하고 아니면 yarr의 값을 취하고 싶다면 리스트 표기법을을 이용해서 다음과 같이 작성할 수 있다.
result = [(x if c else y) for x ,y ,c in zip(xarr, yarr, cond)]
print(result) # [1.1, 2.2, 1.3, 1.4, 2.5]

"""
위 방법은 순수 파이썬으로 수행되기 때문에 큰 배열을 빠르게 처리하지 못한다.
또한 다차원 배열에서는 사용할 수 없는 문제가 있다.
np.where() 를 사용하면 위 문제를 해결할 수 있다.
"""
result = np.where(cond, xarr, yarr)
print(result) #[1.1 2.2 1.3 1.4 2.5]

"""
np.where 의 두 번째 인자와 세 번째 인자는 배열이 아니어도 상관없다. 둘 중 하나 혹은 둘 다 스칼라값이어도
동작한다. 데이터 분석에서 일반적인 where 의 사용은 다른 배열에 기반한 새로운 배열을 생성한다.
임의로 생성된 데이터가 들어 있는 행렬이 있고 양수는 모두 2로, 음수는 모두 -2로 바꾸려면 np.where 를 사용해서 쉽게 처리할 수 있다.
"""
arr = np.random.randn(4,4)
print(arr)
print(arr > 0)
result = np.where(arr > 0, 2, -2) # 양수 일 때 2 , 음수 일 때 -2
print(result)

result = np.where(arr > 0, arr, -2) # 음수 일 때만 -2
print(result)
