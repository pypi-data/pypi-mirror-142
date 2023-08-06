#!/usr/bin/env python


from setuptools import setup, find_packages

setup(
    name="urw",
    py_modules=['urw'],
    version="0.0.7",
    keywords=["urdu", "random", "words", "generator"],
    description="Urdu word/phrase generator.",
    long_description=open('README.md').read(),

    project_urls={
        'Homepage': 'https://www.techtum.dev/work-urw-220310.html',
        'Source': 'https://github.com/siphr/urw',
        'Tracker': 'https://github.com/siphr/urw/issues',
    },
    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['urw'],
    package_data = {
        'urw':['wordlist.txt']
        },
    platforms="any",
    install_requires=[]
)
