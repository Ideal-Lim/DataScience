"""
불리언 배열을 위한 메서드
이전 메셔드의 불리언값을 1 또는 0으로 강제할 수 있다.
따라서 sum 메서드를 실행하면 불리언 배열에서 True 인 원소의 개수를 셀 수 있다.
"""
import numpy as np
arr = np.random.randn(100)
print((arr > 0).sum()) # 0 보다 큰 값들의 합
bools = np.array([False, False, True, False])
# any : 하나 이상의 값이 True 인지 검사
print(bools.any())
# all : 모든 원소가 True 인지 검사
print(bools.all())