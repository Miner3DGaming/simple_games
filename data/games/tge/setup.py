from setuptools import setup, find_packages

from .__init__ import __version__, __author__, __doc__, __name__

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    description=__doc__,
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
)


