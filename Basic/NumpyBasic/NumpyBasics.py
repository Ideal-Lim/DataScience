import numpy as np
import time
"""
Numpy vs List 성능 테스트
"""

if __name__ == "__main__":
    my_arr = np.arange(1000000)
    my_list = list(range(1000000))

    start = time.time()
    for _ in range(10): myarr2 = my_arr * 2
    end = time.time()
    print("{0}".format(end - start))
    start = time.time()
    for _ in range(10): myList2 = [x * 2 for x in my_list]
    end = time.time()
    print("{0}".format(end - start))


