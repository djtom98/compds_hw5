import os, sys
from setuptools import setup, find_packages

# base_dir = os.path.dirname(__file__)
# sys.path.insert(0, src_dir = os.path.join(base_dir, 'src'))

# Package meta-data.
NAME = 'hw5library'
DESCRIPTION = 'Homework 5 Library.'
URL = 'https://github.com/djtom98/compds_hw5'
AUTHOR = 'Sam Minors, Davis Thomas, Pearl Herrero, Shaney Sze'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    install_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    package_dir={'': 'src'},
    include_package_data=True
)