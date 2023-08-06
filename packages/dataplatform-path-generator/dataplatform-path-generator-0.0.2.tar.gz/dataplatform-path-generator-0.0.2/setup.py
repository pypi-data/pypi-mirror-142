import os
from setuptools import setup

setup(
    name="dataplatform-path-generator",
    version="0.0.2",
    author="Yash Vaidya",
    packages=[
        'pathgenerator',
    ],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="A library for generating the path to write files to in cloud storage",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="Apache 2.0",
)