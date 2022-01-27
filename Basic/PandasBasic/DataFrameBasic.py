"""
DataFrame
마치 엑셀(표) 같은 스프레드시트 형식의 자료구조이고 여러 개의 컬럼이 있는데
각 컬럼은 서로 다른 종류의 값을 담을 수 있다. DataFrame은 로우와 컬럼에 대한
색인을 가지고 있는데, 색인의 모양이 같은 Series 객체를 담고 있는 파이썬 사전으로
생각하면 된다. 내부적으로 데이터는 리스트나 사전 또는 1차원 배열을 담고 있는 다른 컬렉션이
아니라 하나 이상의 2차원 배열에 저장된다.
"""

# dataFrame 객체 생성 방법: 같은 길이의 리스트에 담긴 사전 사용 or Numpy 배열 사용
import numpy as np
import pandas as pd

data = {
    # 리스트의 길이가 같아야 됨.
    'alphabet': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'number': [1, 2, 3, 4, 5, 6, 7]
}

frame = pd.DataFrame(data)
print(frame)
# 상위 5개 데이터 출력
print(frame.head())

# number 데이터 만 출력
print(pd.DataFrame(data, columns=['number']))
# number, alphabet 순으로 출력 / 'name' 과 없는 값을 넘기면 Nan 출력
print(pd.DataFrame(data, columns=['number', 'alphabet', 'name']))

frame2 = pd.DataFrame(data, index = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'])
# alphabet column 만 출력
print(frame2['alphabet'])

# 그러면 row 접근은 어떻게? -> loc 사용
print(frame2.loc['one'])

# 칼럼은 대입이 가능하다.
frame2['name'] = "no"
print(frame2)

name = pd.Series(['영수', '철수', '미영'], index = ['two', 'five', 'eight'])
# Series 대입 시 DataFrame 의 색인에 따라 값이 대입되며 존재하지 않는 색인에는 Nan 대입
frame2['name'] = name
print(frame2)
print(frame2.number)

# 데이터 확인
frame2['hasName'] = pd.notna(frame2.name)
frame2['noName'] = pd.isna(frame2.name)
print(frame2)

# column 삭제
del frame2['hasName']
# 여러개 column 은 삭제 안됨
# del frame2['hasName', 'noName']
print(frame2)

"""
DataFrame의 색인을 이용해서 얻은 컬럼은 내부 데이터에 대한 뷰이며 복사가 이루어지지 않는다.
따라서 Series 객체에 대한 변경은 실제 DataFrame에 반영된다.
복사본이 필요할 때는 Series 의 copy() 를 사용한다. 
"""
