import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt

"""
Series 
일련의 객체를 담을 수 있는 1차원 배열 같은 자료구조이다.
색인은 배열의 데이터와 연관된 이름을 가지고 있다.
"""
# index(색인) 와 data 로 이루어짐.
obj = pd.Series([4,7,-1,2])
print(obj)

# values (data) / index
print(obj.values) # [4  7 -1  2]
print(obj.index) # RangeIndex(start=0, stop=4, step=1)

obj2 = pd.Series([4, 7, -5, 3], index=['a', 'b', 'a', 'c'])
print(obj2)
print(obj2.index) # index 가 중복되도 상관없다.
print(obj2['a']) # index 가 a 인 값 모두 출력
print(obj2[['c', 'a', 'b']]) # c, a, b 순서로 출력
print('b' in obj2) # True
print(4 in obj2) # False -> 색인으로 검색

print(obj2 > 0)
print(obj2[obj2 < 0])
print(obj2 * 2)
print(np.exp(obj2))

"""
Series -> 고정 길이의 정렬된 사전형이라고 생각하면 된다.
색인값에 데이터값을 맵핑하고 있으므로 파이썬의 사전형과 비슷하다.
Series 객체는 파이썬의 사전형을 인자로 받아야 하는 많은 함수에서 사전형을 대체하여 사용할 수 있다.
"""

# 파이썬 사전형 -> Series 객체
dictData = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
obj3 = pd.Series(dictData)

print(obj3)
alphabet = ['a', 'b', 'c', 'e']
# 색인 검색
obj4 = pd.Series(dictData, index = alphabet)
print(obj4)

# 누락된 데이터 찾기
# null -> True / not null -> False
print(pd.isnull(obj4))
# null -> False / not null -> True
print(pd.notnull(obj4))

print(obj3 + obj4)

# data 이름
obj4.name = 'num'
# index 이름
obj4.index.name = 'alphabet'
print(obj4)

# index 값 변경
obj4.index = ['e', 'f', 'g', 'h']
print(obj4)




