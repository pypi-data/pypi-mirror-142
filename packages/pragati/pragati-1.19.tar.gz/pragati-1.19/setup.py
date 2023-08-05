from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.19'
DESCRIPTION = 'a pragati module '

# Setting up
setup(
    name="pragati",
    version=VERSION,
    author="The Garbage Minded Man",
    description=DESCRIPTION,
    packages=find_packages(),
    keywords=['Garbage', 'Guido Van Rossum'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ]
)