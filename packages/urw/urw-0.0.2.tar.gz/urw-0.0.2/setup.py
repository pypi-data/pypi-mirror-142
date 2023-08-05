#!/usr/bin/env python


from setuptools import setup, find_packages

setup(
    name="urw",
    py_modules=['urw'],
    version="0.0.2",
    keywords=["urdu", "random", "words", "generator"],
    description="Urdu word/phrase generator.",
    long_description=open('README.md').read(),

    bugtrack_url="https://github.com/siphr/urw.git",
    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['urw'],
    package_data = {
        'urw':['wordlist.txt']
        },
    platforms="any",
    install_requires=[]
)
