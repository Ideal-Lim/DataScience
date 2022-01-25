"""
계단 오르내리기 예제
"""
# 내장 함수 random 사용
import random
import numpy as np
import matplotlib.pyplot as plt
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
plt.plot(walk[:100])
plt.show()

# numpy.random 모듈 사용
draws = np.random.randint(0, 2, size=steps)
steps = np.where(draws > 0, 1, -1) # where(조건, 양수, 음수) -> 양수는 1로 음수는 -1로
walk = steps.cumsum()
print(walk) # 과정확인
print(steps.sum()) # 최종 결과
print(walk.min())
print(walk.max())

# 한번에 시뮬레이션하기 시행횟수 늘리기
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0,2, size=(nwalks, nsteps)) # 0 또는 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)
# print(walks.shape)

# 특정 시점 계산
hits20 = (np.abs(walks) >= 20).any(1) # any()메서드를 사용해서 절댓값 20을 도달 or 넘었는지 확인
print(hits20)

print(hits20.sum()) # 절댓값 20을 넘는 경우의 수

print(walks[hits20]) # 절댓값이 넘는 행만 가져옴
crossing_times = (np.abs(walks[hits20]) >= 20).argmax(1)
print(crossing_times)
print(crossing_times.mean())
