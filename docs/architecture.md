# Architecture

## Overview

The project is organized into three primary modular layers for clarity and maintainability:

- **CLI Layer (`cli.py`)**: Handles user interaction, command parsing, and dispatching to logic modules.
- **Domain Layer (`books.py`)**: Contains pure functions for all business logic (add, edit, open, list books) and serves as the application's engine.
- **Storage Layer (`storage.py`)**: Manages reading, writing, backup, and restoration of JSON data files for persistence.
- **Configuration (`config.py`)**: Centralizes file paths and directory management.
- **Compatibility (`variables.py`)**: Reserved for legacy or compatibility settings.

## Data Flow

User input → CLI → Domain Logic → Storage (and reverse for outputs). All persistent data is stored in `data/data.json` (primary) and `data/data_backup.json` (backup).

## Non-functional Focus

- **Reliability**: Error handling in file I/O, test coverage.
- **Maintainability**: Separated modules, clear documentation.
- **Usability**: Simple text commands, clear prompts, built-in help.

## Extensibility

Future enhancements (like a GUI) can be added in separate modules (e.g., `ui.py`) without disturbing the existing CLI-workflow.
