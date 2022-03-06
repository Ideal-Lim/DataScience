"""
Numpy 는 디스크에서 텍스트나 바이너리 형식의 데이터를 불러오거나 저장할 수 있다.
"""
import numpy as np
arr = np.arange(10)
np.save('some_array', arr) # some_array.npz 로 저장
np.load('some_array.npz')
# savez : 여러 개의 배열을 압축된 형식으로 저장할 수 있다. 저장하려는 배열의 키워드 인자 형태로 전달한다.
np.savez('array_archive.npz', a=arr, b=arr)
arr = np.load('array_archive.npz')
arr['b']
# savez_compressed : 압축이 잘되는 형식의 데이터일 경우 사용
np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)
