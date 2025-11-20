# Book Manager (CLI)
A simple and reliable command-line application to track books and their page counts using a modular Python structure and JSON file storage.

## Features

- Add new books and their current page number
- Edit the page number of existing books
- View all books at a glance
- Open a book to see its last read page
- Backup and restore your book database with a single command
- Command-line interface with helpful prompts
- Modular code structure (CLI, Logic, Storage)

## Tech Stack

- Python 3.10+
- Standard Library (json, pathlib)
- [pytest](https://pytest.org) for testing

## Folder Structure

project/
│
├─ src/
│   └─ bookmgr/
│       ├─ cli.py
│       ├─ books.py
│       ├─ storage.py
│       ├─ config.py
│       ├─ variables.py
│       └─ __init__.py
├─ data/
│   ├─ data.json
│   └─ data_backup.json
├─ tests/
│   ├─ test_books.py
│   └─ test_storage.py
├─ docs/
│   ├─ architecture.md
│   ├─ workflow.md
│   ├─ use-case.md
│   ├─ sequence.md
│   ├─ er-schema.md
│   └─ class-component.md
├─ requirements.txt
├─ README.md
└─ statement.md


## Getting Started
Create a virtual environment and install dependencies:
python -m venv .venv
. .venv/Scripts/activate # On Windows
. .venv/bin/activate # On Mac/Linux
pip install -r requirements.txt

## Run the CLI program:
python -m bookmgr

## How to Test
Run all tests using:
pytest

or (if needed):
PYTHONPATH=src pytest


## Non-Functional Requirements
- Usability: Clear prompts and help instructions in CLI
- Reliability: Backup/restore of data, safe error handling
- Maintainability: Modular files, flat JSON storage structure
- Testability: Automated `pytest` unit tests for main features

## License
Open source under the MIT License.


