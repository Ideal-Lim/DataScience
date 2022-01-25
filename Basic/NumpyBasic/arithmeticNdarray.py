"""
numpy 의 중요한 특징은 for 문을 작성하지 않고 데이터를 일괄 처리할 수 있다는 것이다.
이를 벡터화라고 한다. 같은 크기의 배열 간의 산술 연산은 배열의 각 원소 단위로 적용된다.
"""
import numpy as np
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr * arr)
print(arr ** 2)
print(1/arr)

arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr2 > arr)
"""
[[False  True False]
 [ True False  True]]
 """

"""
크기가 다른 배열 간의 연산은 브로드 캐스팅
"""