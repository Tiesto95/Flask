# Задача 1
from contextlib import contextmanager

class Lock(object):
    def __init__(self):
        self.lock = False

@contextmanager
def lock_on(some_true):
    some_true.lock = True
    yield some_true

with lock_on(Lock):
    print(Lock.lock)

# Задача 2
# from contextlib import contextmanager
# @contextmanager
# def no_exceptions():
#     try:
#         yield
#     except Exception as e:
#         print(e)
#
# with no_exceptions() as f:
#     1 / 0
#     2 + 'sdfdf'
#
# print('done')

# Задача 3
# import time
#
# class TimeIt():
#     def __init__(self):
#         self.time = None
#
#     def __enter__(self):
#         self.time = time.time()
#         return self
#
#     def __exit__(self, *args):
#         self.time = time.time() - self.time
#
# def func_test():
#     time.sleep(2)
#
#
# with TimeIt() as t:
#     func_test()
#
# print('Затраченное время: ', t.time)