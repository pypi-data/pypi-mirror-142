from setuptools import setup, find_packages

VERSION = '0.0.13'
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
    install_requires=['sentry-sdk>=1.5.7', 'aws-xray-sdk>=2.4.3', 'boto3>=1.21.17'],
    url='https://macaiapp.com',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)