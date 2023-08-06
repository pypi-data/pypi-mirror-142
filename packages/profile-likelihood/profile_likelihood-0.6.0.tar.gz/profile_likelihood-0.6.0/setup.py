#!/usr/bin/env python
import pkg_resources
import setuptools
import re

# List of dependecy packages
install_requires = [
    "pytest>=6.2.2",
    "numpy>=1.19.0",
    "scipy>=1.5.0",
    "matplotlib>=3.3.4",
    "pyqt5>=5.13.0",
    "numpydoc>=1.1.0",
]

# Find packages
packages = setuptools.find_packages(exclude=["tests", "docs"])

# Description of the package
description = "Profile likelihood toolbox"
with open("README.md") as f:
    long_description = f.read()

# Get the current version number
with open("profile_likelihood/__init__.py") as fd:
    version = re.search('__version__ = "(.*)"', fd.read()).group(1)


setuptools.setup(
    name="profile_likelihood",
    version=version,
    author="Yonatan Kurniawan",
    author_email="kurniawanyo@outlook.com",
    url="https://git.physics.byu.edu/yonatank/profile_likelihood",
    license="MIT",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    packages=packages,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    python_requires=">=3.6",
)
