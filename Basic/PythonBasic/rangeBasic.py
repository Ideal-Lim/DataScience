# range() : 연속된 숫자(정수)를 만들어주는 메서드
# 0, 1, 2, 3, ... ,9 까지 생성
print(range(10)) # range 객체 range(0, 10)
print([range(10)]) # [range(10)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(start, stop)
print(range(1, 10)) # 1 ~ 9
# range(start, stop, step)
print(range(1, 10, -1)) # 9 ~ 1

# range 객체는 iterable -> for 문 사용가능
