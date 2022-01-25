import numpy as np
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
alphabet = np.array(['a','b','c','d'])
data = np.random.randn(7,4)

print(names == 'Bob') # [ True False False  True False False False]
print(data[names == 'Bob']) # index = 0,3 인 행
print(data[names == 'Bob', 2:]) # index = 0,3 인 행에서 3번째 element 부터 끝까지
print(data[~(names == 'Bob')]) # ~ 를 통해 부정
print((names == 'Bob') | (names == 'Will')) # [ True False  True  True  True False False]
print(data[(names == 'Bob') | (names == 'Will')])
print(data[:,alphabet == 'a']) # index = 0 인 열





