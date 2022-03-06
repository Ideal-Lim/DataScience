import numpy as np
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
alphabet = np.array(['a','b','c','d', 'a', 'a', 'b'])
data = np.random.randn(7,7)

print(names == 'Bob') # [ True False False  True False False False]
print(data[names == 'Bob']) # index = 0,3 인 행
print(data[names == 'Bob', 2:]) # index = 0,3 인 행에서 3번째 element 부터 끝까지
print(data[~(names == 'Bob')]) # ~ 를 통해 부정
print((names == 'Bob') | (names == 'Will')) # [ True False  True  True  True False False]
print(data[(names == 'Bob') | (names == 'Will')])


print(alphabet == 'a') # [ True False False False  True  True False]
print(alphabet != 'a') # [False  True  True  True False False  True]
print((alphabet == 'a') | (alphabet == 'b')) # [ True  True False False  True  True  True]

print(data[alphabet == 'a']) # index = 0,4,5 인 행
print(data[~(alphabet == 'a')]) # ~ 를 통해 부정 / index = 0,4,5 외 나머지 행
print(data[alphabet == 'a', 2:]) # index = 0,4,5 인 행에서 3번째 element 부터 끝
data[data < 0] = 0
print(data)


