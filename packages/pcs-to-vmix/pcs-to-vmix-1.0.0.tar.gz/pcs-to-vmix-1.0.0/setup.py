#!/usr/local/env python3
# Engine's setup.py
import os
import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "../README.md").read_text()

setup(
    name="pcs-to-vmix",
    version="1.0.0",
    description="Interface between PCS scoring data and vMix telnet API",
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
                'pcs_to_vmix = pcs_to_vmix.tcpclient:main',
            ]
    }
)