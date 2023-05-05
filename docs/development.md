# Development

## Create virtual environment

```bash
# create virtual environment
poetry config virtualenvs.in-project true
poetry install

# activate virtual environment
poetry shell

# install python requirements
poetry install

# add a dependency
poetry add <dependency>

# add a dev dependency
poetry add <dependency> -D

# deactivate virtual environment
deactivate
```

## Run tests

```bash
poetry run pytest
```