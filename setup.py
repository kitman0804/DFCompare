# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='DFCompare',
    version='0.1.1',
    description='Compare pandas DataFrames.',
    long_description='Compare pandas DataFrames.',
    keywords=[
        'pandas'
    ],
    url='https://github.com/kitman0804/DFCompare',
    author='perrykmc',
    author_email='kitman0804@gmail.com',
    license='MIT',
    packages=[
        'DFCompare'
    ],
    install_requires=[
        'pandas'
    ],
    include_package_data=True,
    zip_safe=False
)

