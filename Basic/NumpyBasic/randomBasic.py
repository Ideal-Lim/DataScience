"""
numpy.random
기존 python random 함수를 보강하여 다양한 종류의 확률분포로부터 효과적으로 표본값 생성하는데 사용
"""
import numpy as np
import time
from random import normalvariate
# 표준정규분포 표본 생성
randomData = np.random.normal(size=(4,4))
print(randomData)
randomData = np.random.normal(size=(4,4))
print(randomData)
# random vs numpy.random 생성 시간 비교
n = 1000000
start = time.time()
randomDataByRandom = [normalvariate(0,1) for _ in range(n)]
end = time.time()
print("{0}".format(end - start))

start = time.time()
randomDataByNumpy = np.random.normal(size = n)
end = time.time()
print("{0}".format(end - start))

"""
numpy.random 이 내장 random 함수보다 매우 큰 표본을 생성하는데 수십 배 이상 빠르다.
0.5340535640716553s
0.01900482177734375s
이는 유사 난수라고 부르는데, 난수 생성기의 시드값에 따라 정해진 난수를 알고리즘으로 생성하기 때문이다.
Numpy 난수 생성기의 시드값은 np.random.seed를 이용해서 변경가능하다.
"""
np.random.seed(1234)

#numpy.random.RandomState를 이용해서 다른 난수 생성기로부터 격리된 난수 생성기를 만들수 있다.
rng = np.random.RandomState(1234)
dataByRandomState = rng.randn(10)
print(dataByRandomState)



