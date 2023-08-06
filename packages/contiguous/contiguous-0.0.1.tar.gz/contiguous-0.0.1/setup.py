from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='contiguous',
    version='0.0.1',
    packages=['tests', 'contiguous'],
    url='https://github.com/bmcollier/contiguous',
    license='3-Clause BSD',
    author='Ben Collier',
    author_email='bencollier@fastmail.com',
    description='COBOL-style flat contiguous data structures for Python'
)
