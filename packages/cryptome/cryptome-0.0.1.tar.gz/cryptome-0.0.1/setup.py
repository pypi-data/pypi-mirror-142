from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cryptome',
    version='0.0.1',
    description='Get crypto price & info fast, no API needed!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Neil Shah',
    author_email='neil@insight3d.tech',
    license='MIT',
    classifiers=classifiers,
    keywords='crypto',
    packages=find_packages(),
    install_requires=['']
)