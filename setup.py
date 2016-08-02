#!/usr/bin/env python
# -*- coding: utf-8 -*-

# +----------------------------------------------------------------------------
# | Imports
# +----------------------------------------------------------------------------
from setuptools import setup, find_packages

# +----------------------------------------------------------------------------
# | Definition of the scripts
# +----------------------------------------------------------------------------
scripts = [
    "pysafe"
]


# +----------------------------------------------------------------------------
# | Definition of the dependencies
# +----------------------------------------------------------------------------
dependencies = []
with open('requirements.txt', 'r') as fd_requirements:
    for dependency in fd_requirements:
        dependencies.append(dependency.strip())

extra_dependencies = {}

dependency_links = []


# Extract the long description from README.md
README = open('README.md', 'rt').read()

# +----------------------------------------------------------------------------
# | Definition of the setup
# +----------------------------------------------------------------------------
setup(
    name="pysafe",
    scripts=scripts,
    install_requires=dependencies,
    extras_require=extra_dependencies,
    dependency_links=dependency_links,
    version="1.0.dev0",
    license="GNU GPLv3",
    description="Yet Another Homade Credential Store",
    long_description=README,
    platforms="Linux_x86, Linux_x64",
    author="Georges Bossert",
    author_email="gbossert@miskin.fr",
    url="https://github.com/gbossert/pysafe"
)
