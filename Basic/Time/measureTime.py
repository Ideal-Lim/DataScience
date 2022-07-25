import time

def measureTime(func):
    start = time.time()
    func()
    end = time.time()
