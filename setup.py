#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-aiglobal',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.aiglobal'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        aiglobal = ckanext.aiglobal.plugins:CustomTheme
    """
)
