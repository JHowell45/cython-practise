from timeit import timeit

FIB_MAX = 10000
MAX = 100000


# timer = timeit(
#     setup="from py_fibonacci import py_fib", stmt=f"py_fib({FIB_MAX})", number=MAX
# )
# print(f"py_fib time: {timer}")


# timer = timeit(setup="from fibonacci import fib", stmt=f"fib({FIB_MAX})", number=MAX)
# print(f"fib time: {timer}")
