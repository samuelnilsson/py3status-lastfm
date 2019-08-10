#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='py3status-lastfm',
    version='0.1.0',
    description='A py3status module for displaying a users currently playing song on last.fm',
    author='Samuel Nilsson',
    author_email='samni698@gmail.com',
    url='https://github.com/samuelnilsson/py3status-lastfm',
    packages=find_packages(where='src'),
    install_requires=['py3status>=3.20', "requests"],
    package_dir={'': 'src'},
    entry_points={'py3status': ['module = py3status_lastfm.lastfm']}
)
