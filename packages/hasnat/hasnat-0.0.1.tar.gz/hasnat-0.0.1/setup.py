from setuptools import setup, find_packages

VERSION = '0.0.1'
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