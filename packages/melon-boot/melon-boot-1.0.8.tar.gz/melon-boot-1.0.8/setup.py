# -*- encoding: utf-8 -*-
"""
py setup.py sdist bdist_wheel
py -m twine upload dist/*

@Author  : zh_o
"""
from setuptools import setup, find_packages


setup(
    name='melon-boot',
    version='1.0.8',
    author='zh_o',
    author_email='isbo.zh@outlook.com',
    description='The ui automation framework',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['toml', 'selenium', 'pytest', 'allure-pytest', 'faker']
)
