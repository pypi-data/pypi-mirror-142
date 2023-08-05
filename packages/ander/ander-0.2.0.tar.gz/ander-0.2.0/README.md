# ander: A CLI tool to identify elements that are contained in both file

![PyPi ver](https://img.shields.io/pypi/v/ander?style=flat-square)
![LICENSE budge](https://img.shields.io/github/license/joe-yama/ander?style=flat-square)

## Basic Usage

```bash
$ cat file1.txt
duplicated
notduplicated

$ cat file2.txt
duplicated
not duplicated

$ ander file1.txt file2.txt
duplicated
```

## Installation

```bash
$ pip install ander
```

### Requirements

- Python >= 3.6
- Some Python Libraries (see `pyproject.toml`)

## License

This software is released under the MIT License, see LICENSE.
