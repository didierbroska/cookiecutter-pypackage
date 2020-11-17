#!/usr/bin/env python
import os
from shutil import copyfile

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    copyfile("README.md", "docs/readme2.md")
    copyfile("CONTRIBUTING.md", "docs/CONTRIBUTING.md")
    copyfile("HISTORY.md", "docs/HISTORY.md")
    copyfile("AUTHORS.md", "docs/AUTHORS.md")

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")
        remove_file("docs/AUTHORS.md")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")
