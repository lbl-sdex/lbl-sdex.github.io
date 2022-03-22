#!/usr/bin/env python

"""The setup script."""
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]

with open(path.join(here, 'requirements-docs.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements_docs = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]

setup(
    author="Ronald J Pandolfi",
    author_email='ronpandolfi@lbl.gov',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    description="SDEX Group",
    entry_points={
        'console_scripts': [
            #'sdex_group=sdex_group:some_function',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='sdex_group',
    name='sdex_group',
    packages=find_packages(include=['sdex_group', 'sdex_group.*']),
    test_suite='tests',
    url='https://github.com/lbl-sdex/sdex_group',
    zip_safe=False,
    extras_require={
        'docs': ['sphinx', 'sphinx-rtd-theme', 'myst-parser', 'myst-nb', 'sphinx-panels', 'autodocs']
    }
)
