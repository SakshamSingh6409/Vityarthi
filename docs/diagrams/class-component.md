# Class/Component View

**Components:**
- CLI (cli.py): Input loop, parsing, help, error display.
- Domain Logic (books.py): add_book, edit_book, open_book, show_all (all pure functions, operate on book list).
- Storage (storage.py): read_data, write_data, backup, restore (all handle file operations).
- Configuration (config.py): Paths to data/backup for maintainable file management.
- Compatibility (variables.py): Reserved for compatibility or future settings.

**Relations:**
- CLI imports domain logic and storage modules.
- Domain and storage do not import from each other (loose coupling).
- Storage imports config for consistent file paths.

**Visualization (Text):**
CLI → Domain Logic → (in-memory list)
CLI → Storage → (file I/O)
Storage → Config → (paths)