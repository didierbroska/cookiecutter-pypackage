{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{%- if is_open_source %}
- Free software: {{ cookiecutter.open_source_license }}
{%- endif %}
- Documentation : TODO

## Features

- TODO

## Credit

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [didierbroska/cookiecutter-pypackage](https://github.com/didierbroska/cookiecutter-pypackage) project template.
