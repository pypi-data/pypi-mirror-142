from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Macai framework for AWS lambda in Python'
LONG_DESCRIPTION = 'Macai framework for AWS lambda in Python'

setup(
    name="framework-python",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Macai",
    author_email="developers@macaiapp.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='conversion',
    url='https://macaiapp.com',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)