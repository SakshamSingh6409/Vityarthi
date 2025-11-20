# Testing

## Scope

This project uses simple unit tests to ensure the core modules (book management logic and storage) work as expected. The approach focuses on testing core functionality for correctness and reliability.

## Method

- `test_books.py`: Tests adding, editing, and opening books in memory through pure functions defined in `books.py`.
- `test_storage.py`: Tests reading, writing, backup, and restore behavior for JSON book data files using temporary paths.

Tests are automated using `pytest`. Running `pytest` from the project root will execute all test cases and report any failures.

## How to Run
python -m pytest -q
or, with the virtual environment active:

## Notes

- Test files are located in the `tests/` folder for clear separation.
- Temporary files are used where needed to avoid modifying actual data during test runs.
- Manual validation of the CLI is also possible by running the application and using different book commands.
