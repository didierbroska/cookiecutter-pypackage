# coding: utf-8

import datetime
import os

from helpers import bake_in_temp_dir, run_inside_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        # Inside top level folder
        found_toplevel_files = [f.basename for f in result.project.listdir()]

        ## Markdown files
        assert "README.md" in found_toplevel_files
        assert "AUTHORS.md" in found_toplevel_files
        assert "CONTRIBUTING.md" in found_toplevel_files
        assert "HISTORY.md" in found_toplevel_files

        assert "LICENSE" in found_toplevel_files

        ## Folders
        assert ".github" in found_toplevel_files
        assert "python_boilerplate" in found_toplevel_files
        assert "docs" in found_toplevel_files
        assert "tests" in found_toplevel_files

        # Inside docs folder
        doc_files = [f.basename for f in result.project.join("docs").listdir()]
        assert "index.md" in doc_files
        assert "installation.md" in doc_files
        assert "modules.md" in doc_files
        assert "usage.md" in doc_files

        ## imported markdown files
        assert "readme2.md" in doc_files
        assert "HISTORY.md" in doc_files
        assert "CONTRIBUTING.md" in doc_files
        assert "AUTHORS.md" in doc_files

        # Inside tests folder
        test_files = [
            f.basename for f in result.project.join("tests").listdir()
        ]
        assert "__init__.py" in test_files
        assert "conftest.py" in test_files
        assert "test_python_boilerplate.py" in test_files


def test_bake_without_author_file(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"create_author_file": "n"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "AUTHORS.md" not in found_toplevel_files
        doc_files = [f.basename for f in result.project.join("docs").listdir()]
        assert "AUTHORS.md" not in doc_files

        # Assert no Authors in MkDocs config
        mkdocs = result.project.join("mkdocs.yml")
        with open(str(mkdocs)) as index_file:
            assert "- Authors: AUTHORS.md" not in index_file.read()

        # Assert there are no spaces in the toc tree
        docs_index_path = result.project.join("docs/index.md")
        with open(str(docs_index_path)) as index_file:
            assert "- [Authors](./AUTHORS.md)" not in index_file.read()

        # Assert not authors in pyproject.toml
        pyproject = result.project.join("pyproject.toml")
        with open(str(pyproject)) as index_file:
            assert (
                'authors = ["Didier Bröska <didier.broska>@example.com"]'
                not in index_file.read()
            )


def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join("LICENSE")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def test_bake_selecting_license(cookies):
    license_strings = {
        "MIT license": "MIT ",
        "BSD license": "Redistributions of source code must retain the "
        + "above copyright notice, this",
        "ISC license": "ISC License",
        "Apache Software License 2.0": "Licensed under the Apache License, Version 2.0",
        "GNU General Public License v3": "GNU GENERAL PUBLIC LICENSE",
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(
            cookies, extra_context={"open_source_license": license}
        ) as result:
            assert target_string in result.project.join("LICENSE").read()
            assert license in result.project.join("README.md").read()
            assert license in result.project.join("pyproject.toml").read()
            # TODO add test for classifier
            # TODO add test for include


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "LICENSE" not in found_toplevel_files
        assert "License" not in result.project.join("README.md").read()
        assert "license =" not in result.project.join("pyproject.toml").read()
        # TODO add test for classifier
        # TODO add test for include


def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        if os.name == "nt":
            run_inside_dir(
                "%USERPROFILE%\\.poetry\\bin\\poetry install -v",
                str(result.project),
            ) == 0
            run_inside_dir(
                "%USERPROFILE%\\.poetry\\bin\\poetry run pytest",
                str(result.project),
            ) == 0
        else:
            run_inside_dir("poetry install -v", str(result.project)) == 0
            run_inside_dir("poetry run pytest", str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


def test_bake_with_no_console_script(cookies):
    context = {"command_line_interface": "No command-line interface"}
    result = cookies.bake(extra_context=context)
    project_files = [
        f.basename for f in result.project.join("python_boilerplate").listdir()
    ]
    assert "cli.py" not in project_files

    setup_path = result.project.join("pyproject.toml")
    with open(str(setup_path), "r") as setup_file:
        assert "[tool.poetry.scripts]" not in setup_file.read()


def test_bake_with_console_script_files(cookies):
    context = {"command_line_interface": "click"}
    result = cookies.bake(extra_context=context)
    project_files = [
        f.basename for f in result.project.join("python_boilerplate").listdir()
    ]
    assert "cli.py" in project_files

    setup_path = result.project.join("pyproject.toml")
    with open(str(setup_path), "r") as setup_file:
        assert "[tool.poetry.scripts]" in setup_file.read()


# TODO test specials chars
