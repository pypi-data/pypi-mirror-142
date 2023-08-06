from setuptools import setup

with open('README.md','r') as fh:
    long_desc = fh.read()
setup(
    name='backpropagation',
    version='0.0.3',
    description='Backpropagation Algorithm',
    packages=['backpropagation'],
    classifiers=["Intended Audience :: Education", 
    "Operating System :: OS Independent", 
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8"],
    long_description=long_desc,
    long_description_content_type="text/markdown",
    install_requires=['numpy']
)