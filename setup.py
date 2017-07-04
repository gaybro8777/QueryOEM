#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['beautifulsoup4','requests']

setup(
    name='QueryOEM',
    version='1.0.0',
    description=('Query OEM for product informations'),
    long_description=readme + '\n\n' + history,
    author="Fabricio Roberto reinert",
    author_email='fabricio.reinert@live.com',
    url='https://github.com/FRReinert/StationScrapping',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='OEM, Dell, Python, Web, Scrapping, JSON',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)
