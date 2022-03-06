"""
색인 객체 (Index Objects)
pandas 의 색인 객체는 표 형식의 데이터에서 각 로우와 컬럼에 대한 이름과 다른 메타데이터(축의 이름 등)을 저장하는 객체이다.
Series나 DataFrame 객체를 생성할 때 사용되는 배열이나 다른 순차적인 이름은 내부적으로 색인으로 변환된다.
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
obj = pd.Series(range(3), index=['a', 'b', 'c'])
# index 객체
index = obj.index
print(index)
print(index[1:])
print(index[:-1])

# 색인객체는 변경이 불가능하다. ex) index[1] = 'f' -> Error!
labels = pd.Index(np.arange(3))
print(labels)

obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)

print(obj2.index is labels)

# Index는 중복된 값을 허용한다.
duplication_labels = pd.Index(['a', 'a', 'b', 'c'])
print(duplication_labels)
