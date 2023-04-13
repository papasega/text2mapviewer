from setuptools import setup, find_packages

"""
    [build-system]
requires = ["setuptools>=65.6.3"]
build-backend = "setuptools.build_meta"
"""

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Science/Research',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='text2mapview',
    version='0.2.0',
    description='A python package to map your own csv files data using Atlas from NOMIC',
    # + '\n\n' + open('CHANGELOG.md').read(),
    long_description=open('README.md').read(),
    url='https://github.com/papasega/text2mapview',
    author='Papa Séga WADE',
    author_email='pasega.wade@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Embedding, Visualization, Map, Text, CSV, Search keywords, Dynamic',
    packages=find_packages(),
    install_requires=['requirements.txt']
)
