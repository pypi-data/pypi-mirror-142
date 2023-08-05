from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.11'
DESCRIPTION = 'Hasnat Library'

classifiers=[
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
]


setup(
  name='hasnat',
  version=VERSION,
  description=DESCRIPTION,
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://hasnat.io',  
  author='Hasnat Abdul',
  author_email='abdul@hasnat.io',
  license='MIT', 
  classifiers=classifiers,
  keywords='hasnat', 
  packages=find_packages(),
  install_requires=[''] 
)