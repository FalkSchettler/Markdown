# Developer Documentation

## Select Interpreter

- Recommended Python Interpreter version: 3.12.x

## Create Virtual Environment and Install Dependencies

### Visual Studio Code

Within Visual Studio Code, you can directly create a virtual environment:

- Press `Ctrl+Shift+P`, search for `Python: Create Environment`, and select `Venv`.
- Based on a local Python installation (recommended 3.12.x), create a local workspace environment.

## Install Poetry

- Open the terminal and install Poetry in your current virtual environment. The version depends on the version specified in the [pyproject.toml](../../pyproject.toml).

```sh
pip install poetry>=1.5.0
```

From now on, all dependencies are handled with Poetry.

## Use Poetry to Install Dependencies

```sh
poetry install .
```

