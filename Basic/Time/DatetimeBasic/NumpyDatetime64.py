import numpy as np
print(type(np.datetime64('2022-01-01')))

# dtype datetime64으로 설정하기
arr1 = np.array(['2022-01-01','2022-01-02','2022-01-03'])
print(type(arr1[0]))

arr2 = np.array(['2022-01-01','2022-01-02','2022-01-03'], dtype='datetime64')
print(type(arr2[0]))

# arange(), 시작날짜와 마지막 날짜 사이 값 구하기 / dtype 으로 범위 설정 [D] : 날짜, [M] : 달 이를 단위코드라 한다.
print(np.arange('2022-07-01', '2022-08-12', dtype='datetime64[D]')) # 12일 포함 x 리스트와 동일
print(np.arange('2022-07-01', '2022-08-12', dtype='datetime64[M]'))
