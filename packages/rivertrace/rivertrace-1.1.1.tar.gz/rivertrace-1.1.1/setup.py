# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rivertrace',
    version='1.1.1',
    description='Identifies rivers in satellite images and generates a path of pixel values along its length.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='James Runnalls',
    author_email='runnalls.james@gmail.com',
    url='https://github.com/JamesRunnalls/river-trace',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
            'numpy',
            'scikit-image',
            'networkx==2.3.0',
        ]
)
