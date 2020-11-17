# Cookiecutter PyPackage (Broska Version)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter
) template for Python package.

- GitHub repo : https://github.com/didierbroska/cookiecutter-pypackage/
- Documentations : TODO
- Free software : MIT license

## Features

- Multi Python versions manager with [pyenv](https://github.com/pyenv/pyenv).
- Testing setup with [pytest](https://docs.pytest.org/en/stable/).
- Dependancies manager with [poetry](https://python-poetry.org/).
- [Tox](https://tox.readthedocs.io/en/latest/) testing : Setup to easily test for Python 3.6, 3.7, 3.8 and 3.9.
- Security checking with [safety](https://github.com/pyupio/safety).
- Documentations ready with [MkDocs](https://www.mkdocs.org/).
- Change version with [poetry](https://python-poetry.org/).
- Auto release to [PyPI](https://pypi.org/) when push a new tag to master (optional).
- Command line interface using [Click](https://click.palletsprojects.com/en/7.x/) (optional).
- Integration with [Github actions](https://github.com/features/actions).

## Quickstart

Install the latest Cookiecutter, if you haven't installed it yet :

```bash
$ pip install -U cookiecutter
```

*My prefered way is using [pipx](https://pipxproject.github.io/pipx/).*

```bash
$ pipx install cookiecutter
```

Generate a Python package project :

```bash
cookiecutter gh:didierbroska/cookiecutter-pypackage.git
```

Then :

- Create a repo and put it there.
- Install the dev requirements in your virtualenv. (`poetry install`)
- [Register](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives) your project to PyPI.
- Configure documentations in [Github pages](https://pages.github.com/).
- Release your package by pushing a new tag to master.
- Add a couple of `pyproject.toml/poetry.lock` files that specities the packages you will need for your project and their versions. For more informations see the [poetry version constraints](https://python-poetry.org/docs/dependency-specification/) and [the pyproject.toml file](https://python-poetry.org/docs/pyproject/).
- Use [safety](https://github.com/pyupio/safety) for security check (`safety check`).

For more details, see the [cookiecutter-pypackage tutorial](#) *TODO link documentations*

## Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork this to create your own version. Or create your own; it doesn't strictly have to be a fork.

- Once you have your own version working, add it to the Similar Cookiecutter Templates list above with a brief description.

- It's up to you whether or not to rename your fork/own version. Do whatever you think sounds good.

## Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if they make my own packaging experience better.

---

*This repository is inspirated by the original's [Audrey Feldroy cookiecutter pypackage template](https://github.com/audreyfeldroy/cookiecutter-pypackage).*
