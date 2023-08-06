#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="c19",
    version="0.0.7",
    keywords=["covid-19", "stats", "distribution", "Pakistan"],

    description="COVID-19 stats package for the country of Pakistan.",
    long_description=open('README.md').read(),

    project_urls={
        'Homepage': 'https://www.techtum.dev/work-c19-220109.html',
        'Source': 'https://github.com/siphr/c19',
        'Tracker': 'https://github.com/siphr/c19/issues',
    },

    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['c19'],
    package_data = {
        'c19':['countries/*']
        },
    platforms="any",
    install_requires=[]
)
