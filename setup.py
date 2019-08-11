#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='py3status-lastfm',
    version='0.1.0',
    description='A py3status module for displaying a users currently playing song on last.fm',
    author='Samuel Nilsson',
    author_email='samni698@gmail.com',
    license='GNU General Public License v3 (GPLv3)',
    keywords=[
        'py3status',
        'lastfm',
        'last-fm',
        'i3',
        'i3wm',
        'sway',
        'swaywm'
    ],
    url='https://github.com/samuelnilsson/py3status-lastfm',
    download_url='https://github.com/samuelnilsson/py3status-lastfm/archive/v0.1.0.tar.gz',
    packages=find_packages(where='src'),
    install_requires=['py3status>=3.20', "requests"],
    package_dir={'': 'src'},
    entry_points={'py3status': ['module = py3status_lastfm.lastfm']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop'
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
