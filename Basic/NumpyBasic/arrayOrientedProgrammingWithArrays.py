"""
Numpy 배열을 사용하면 반복문을 작성하지 않고 간결한 배열 연산을 사용해
많은 종류의 데이터 처리 작업을 할 수 있다. 배열 연산을 사용해서 반복문을 명시적으로 제거하는
기법을 흔히 벡터화라고 부르는데, 일반적으로 벡터화된 배열에 대한 산술 연산을 순수 파이썬 연산에 비해
2~3 배 에서는 많게는 수십, 수백 배까지 빠르다. 브로드캐스팅은 아주 강력한 벡터 연산 방법이다.
"""
import numpy as np
import matplotlib.pyplot as plt
# -5~ 4.99 까지 0.01 증가하는 값들의 배열 생성
arr = np.arange(-5, 5, 0.01)
print(arr)
print(arr.shape)
# meshgrid : 두 개의 1차원 배열을 받아서 가능한 모든 (x, y) 짝을 만들 수 있는 2차원 배열 두 개를 반환한다.
xs, ys = np.meshgrid(arr, arr)
print(xs.shape)
print(xs)
print(ys)

"""
sqrt(x^2 + y^2) 계산
"""
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
"""
matplotlib 시각화
"""
plt.imshow(z, cmap = plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.draw()
plt.close('all')