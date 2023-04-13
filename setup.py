from setuptools import setup, find_packages

"""
    [build-system]
requires = ["setuptools>=65.6.3"]
build-backend = "setuptools.build_meta"
"""

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: ',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Map Embedding Text/CSV Data',
  version='0.1.0',
  description='A python package to map your own csv files data using Atlas from NOMIC',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  url='',  
  author='Papa Séga WADE',
  author_email='pasega.wade@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Embedding, Visualization, Map, Text, CSV,  Search keywords, dynamic', 
  packages=find_packages(),
  install_requires=['requirements.txt'] 
)
