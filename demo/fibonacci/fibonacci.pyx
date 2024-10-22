import cython


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


def optimised_fib(n: cython.int) -> cython.int:
    a: cython.int
    b: cython.int
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b
