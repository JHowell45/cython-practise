import Cython.Compiler.Options
from Cython.Build import cythonize
from setuptools import Extension, setup

Cython.Compiler.Options.annotate = True

extensions = [
    Extension("fibonacci", ["demo/fibonacci/fibonacci.pyx"]),
    Extension("primes", ["demo/primes/primes.pyx"]),
]

setup(
    name="demo",
    ext_modules=cythonize(extensions, annotate=True),
)
