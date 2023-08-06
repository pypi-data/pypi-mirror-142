#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="pyfrx",
    version="0.0.3",
    keywords=["forex", "finance", "conversion", "rates"],

    description="Forex conversion and rates.",
    long_description=open('README.md').read(),

    project_urls={
 'Homepage': 'https://www.techtum.dev/work-pyfrx-220105.html',
        'Source': 'https://github.com/siphr/pyfrx',
        'Tracker': 'https://github.com/siphr/pyfrx/issues',
    },

    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['pyfrx'],
    platforms="any",
)
