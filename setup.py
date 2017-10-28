# setup.py
#
from setuptools import setup, find_packages

import shortwave
import os


def read(*names):
    values = dict()
    extensions = ['.txt', '.rst']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values


long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')


setup(
    version=shortwave.__version__,
    name='shortwave-searcher',
    description='Parse shortwave radio frequency data from eibispace',
    long_description=long_description,
    packages=find_packages(),
    test_suite='shortwave.tests',
)
