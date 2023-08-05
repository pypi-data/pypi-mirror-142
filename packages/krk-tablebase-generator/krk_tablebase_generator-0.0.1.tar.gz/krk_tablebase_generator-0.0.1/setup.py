from setuptools import setup, Extension
import pybind11

cpp_args = ['-std:c++latest']
sfc_module = Extension(
    'tablebase',
    sources=['src/krk_tablebase\\krk_tablebase.cpp'],
    include_dirs=[pybind11.get_include(),"C:/boost_1_78_0/boost_1_78_0"],
    language='c++',
    extra_compile_args=cpp_args,
)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='krk_tablebase_generator',
    version='0.0.1',
    author="Nolan Chu",
    author_email="nolan.chu.2012@gmail.com",
    description='C++ extension package that generates a tablebase of KR_K chess endgames.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    ext_modules=[sfc_module],
)