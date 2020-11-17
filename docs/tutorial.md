# Tutorial

!!! note
    Did you find any of these instructions confusing ? [Edit this file](https://github.com/didierbroska/cookiecutter-pypackage/blob/master/docs/tutorial.md) and submit a pull request with your improvements !

To start with, you will need a [GitHub account](https://github.com/) and an account on [PyPI](https://pypi.python.org/pypi). Create these before you get started on this tutorial. If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at [GitHub Help](https://help.github.com/).

## Step 1 : Install Cookiecutter

First, you need have `pipx`, you can follow [this instruction](https://pipxproject.github.io/pipx/installation/) to install.

Install cookiecutter :

```bash
$ pipx install cookiecutter
```

## Step 2 : Generate your package

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the cookiecutter-pypackage repo:

```bash
$ cookiecutter gh:didierbroska/cookiecutter-pypackage.git
```

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.

## Step 3 : Create a Github repo
