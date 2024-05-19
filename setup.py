from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        name="sensitivity.primary_sensitivity",
        sources=["sensitivity/primary_sensitivity.pyx", "sensitivity/primary_sensitivity_impl.c"],
        language="c",
    )
]

setup(
    name="sensitivity",
    version="0.1",
    description="A package to compute the primary sensitivity of the PCC to new data points",
    author="Marc Harary",
    author_email="marc@ds.dfci.harvard.edu",
    license="MIT",
    packages=["sensitivity"],
    ext_modules=cythonize(ext_modules),
    install_requires=[
        "Cython",
    ],
)
