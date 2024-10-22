from setuptools import Extension, setup

setup(
    name="demo",
    ext_modules=[
        Extension("fibonacci", ["demo/fibonacci/fibonacci.pyx"]),
        Extension("primes", ["demo/primes/primes.pyx"]),
    ],
)
