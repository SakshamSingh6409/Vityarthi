# Changelog

## 0.1.0 — Initial Release

- Modularized codebase into CLI, logic, storage, and config components under `src/bookmgr/`
- Added command-line interface: add book, open book, edit page, show all, backup, restore, help, exit
- Introduced JSON-based persistent storage in `data/` with easy backup/restore functions
- Separated documentation: `README.md`, architecture and workflow docs, use case and ER design
- Provided minimal automated tests for business logic and persistence modules (`pytest`)
- Documented all architectural and workflow choices in `docs/`
- Included clear instructions for testing and usage in `README.md`
