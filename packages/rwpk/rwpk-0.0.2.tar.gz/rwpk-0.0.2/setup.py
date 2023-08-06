#!/usr/bin/env python


from setuptools import setup, find_packages

setup(
    name="rwpk",
    py_modules=['rwpk'],
    version="0.0.2",
    keywords=["pakistani", "urdu", "sindhi", "random", "words", "generator"],
    description="Pakistani word/phrase generator.",
    long_description=open('README.md').read(),

    project_urls={
        'Homepage': 'https://www.techtum.dev/work-rwp-220314.html',
        'Source': 'https://github.com/siphr/rwpk',
        'Tracker': 'https://github.com/siphr/rwpk/issues',
    },
    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['rwpk'],
    package_data = {
        'rwpk':['languages/*']
        },
    platforms="any",
)
