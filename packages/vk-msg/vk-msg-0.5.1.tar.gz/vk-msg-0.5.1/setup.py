from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='vk-msg',
    version='0.5.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    author_email='flikemaster2@gmail.com',
)