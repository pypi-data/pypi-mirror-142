import setuptools
from setuptools import setup

version = "0.0.1"

setuptools.setup(
    name="kitolib",
    version=version,
    author="Kito",
    install_requires=[
        "numpy==1.19.2",
        "matplotlib==3.3.4"
    ],
    packages=setuptools.find_packages()
)