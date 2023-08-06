#!/usr/local/env python3
# Engine's setup.py
import os
import pathlib

from setuptools import setup

# The directory containing this file
PKG_ROOT = pathlib.Path(__file__).parent

# The text of the README file
README = (PKG_ROOT / "README.md").read_text()
print(f'PKG_ROOT:{PKG_ROOT}')
VERSION = VERSION = (PKG_ROOT / "VERSION").read_text() 
# VERSION = '0.0.0'

setup(
    name = "pcs-to-vmix",
    version = VERSION,
    description="Interface between Play Cricket Scorer data and vMix & Companion",
    author="Keith Marston",
    author_email="keith@sneconsulting.co.uk",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/smudge1977/pcs-to-vmix-interface",
    packages=["pcs_to_vmix"],
    install_requires=[
        'lxml',
        
    ],
    entry_points={
        'console_scripts': 
            [
                'pcs_watcher = pcs_to_vmix.tcpclient:main',
            ]
    },

    data_files=[
        ('VERSION', ['VERSION']),
        # ('config', ['cfg/data.cfg']),
    ],

    classifiers=[
        # 'Development Status :: 4 - Beta',
        # 'Environment :: Console',
        # 'Environment :: Web Environment',
        # 'Intended Audience :: End Users/Desktop',
        # 'Intended Audience :: Developers',
        # 'Intended Audience :: System Administrators',
        # 'License :: OSI Approved :: Python Software Foundation License',
        # 'Operating System :: MacOS :: MacOS X',
        # 'Operating System :: Microsoft :: Windows',
        # 'Operating System :: POSIX',
        # 'Programming Language :: Python',
        # 'Topic :: Communications :: Email',
        # 'Topic :: Office/Business',
        # 'Topic :: Software Development :: Bug Tracking',
    ],
)