# Starting a new project

A well-structured and maintainable python project includes very many components, requiring broad and advanced knowledge.
However, tools exist to dramatically simplify this process. The `cookiecutter` tool can allow you to initialize
your project structure with all these components in a good initial state. From there you can explore each component at
your own pace as needed. This process might also be used to improve an existing project with some care. Our custom 
cookiecutter facilitates better programming practices by incorporating CI (GitHub Actions), code metrics (CodeCov), and 
documentation (Sphinx + ReadTheDocs) boilerplate to reduce the barrier-to-entry for setting up these types of tools.

## A bit about `cookiecutter`

Cookiecutter is a python packages that allows you to initialize new projects in various languages with project templates.
Many 'cookiecutters' exist with different components included, and with different purposes. The cookiecutter template 
used here includes the components and structure that our group has identified as most beneficial for starting a new
Python package.

## Using our cookiecutter

First, install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Now you can apply our cookiecutter to initialize a new Python project: 

```
cookiecutter https://github.com/ihumphrey/cookiecutter-pypackage.git
```

Cookiecutter will then ask you a series of questions so that it can populate the project with your own names and chosen
components. Be careful to follow the recommended style for each response, i.e. `project_slug [python_bolerplate]` will
need to be a valid python identifier (no spaces, special characters, etc.).

Your new project directory will then be generated!

## What's in this cookiecutter?

- Standard Python package directory structure that maps to your projects package, subpackages, and modules
- A `setup.py` file and related files that are used for packaging your project
- An empty `requirements.txt` file where you can add python package dependencies
- Standard Python `.gitignore` file
- A workflow file that can be used by GitHub Actions (a continuous integration tool) to:
      - Build and test your code with coverage, upload coverage, and report its status
      - Facilitate automatic PyPI releases and GitHub Releases when pushing tags
- Testing setup with unittest and python setup.py test or pytest
- versioneer: automatically updates your version numbers everywhere at once
- Github actions: starter workflow to automate continuous integration, testing, and deployment
- Tox testing: Setup to easily test for Python 3.6, 3.7, 3.8
- Codecov: See how much of your code is covered by tests
- Sphinx docs: Documentation ready for generation with, for example, Read the Docs
- MyST extension: Adds Markdown support to Sphinx
- A set of licenses to choose from and attach to the project

Not included but recommended:

- [Code Climate](https://docs.codeclimate.com/): Feedback on code quality and maintainability

## What's next?

There are some steps that cookiecutter *can't* do for you. We suggest you follow these remaining steps to take full
advantage of what's in your new project.

- Create a new repository on Github and add it as a remote to your local project.
- Install the dev requirements into a virtualenv. (`pip install -r requirements_dev.txt`)
- Register your project with PyPI to reserve the name and enable distribution.
- Add the repo to your Read the Docs account + turn on the Read the Docs service hook.
- Release your package by pushing a new tag to master.
- Add a requirements.txt file that specifies the packages you will need for your project and their versions. For more info see the pip docs for requirements files.
- Activate your project on [codeclimate.com](https://docs.codeclimate.com/)

Now that you've set up your new project, see some other best practices our group recommends:

...