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
