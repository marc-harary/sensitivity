from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        name="primary_sensitivity",
        sources=["sensitivity/sensitivity.pyx", "sensitivity/students_t.c", "sensitivity/primary_sensitivity_impl.c"],
        include_dirs=["."],  # This ensures the headers are found in the current directory
    )
]

setup(
    name="primary_sensitivity",
    ext_modules=cythonize(ext_modules),
)

