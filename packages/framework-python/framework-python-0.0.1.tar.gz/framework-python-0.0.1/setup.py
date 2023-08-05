# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='framework-python',  # Required
    version='0.0.1',  # Required
    description='Macai framework for AWS lambda in Python', 
    install_requires=['sentry-sdk>=1.5.7', 'aws-xray-sdk>=2.4.3'],
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.6, <4',
    url='https://macaiapp.com',
)