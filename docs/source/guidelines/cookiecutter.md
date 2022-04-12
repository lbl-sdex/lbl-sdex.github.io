# Cookiecutter

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) 
is a utility that can be used to define project templates
and create new projects from these templates.

## Motivation

By writing custom cookiecutters, SDEX can create software projects on GitHub 
that are more standardized and uniform in their project structures.
Additionally, these custom cookiecutters facilitate better programming practices by incorporating
CI (GitHub Actions), code metrics (CodeCov), and documentation (Sphinx + ReadTheDocs)
boilerplate to reduce the barrier-to-entry for setting up these types of tools.

## Python Cookiecutter

To use this cookiecutter, follow [these instructions](https://github.com/ihumphrey/cookiecutter-pypackage#readme).

This cookiecutter provides:

* a `setup.py` file and related files that are used for packaging your project
* a workflow file that can be used by GitHub Actions (a continuous integration tool) to:
  * build and test your code with coverage, upload coverage, and report its status
  * facilitate automatic PyPI releases and GitHub Releases when pushing tags
* a directory structure that maps to your projects package, subpackages, and modules
* the sphinx components required to write markdown (MyST) documentation and build it
* versioning tools (`versioneer`) to automatically add versioning to your project
* an empty `requirements.txt` file where you can add python package dependencies
* a standard Python `.gitignore` file
* a set of licenses to choose from and attach to the project
