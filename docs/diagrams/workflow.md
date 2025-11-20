# Workflow

1. **Start application**: Load books from `data.json` if available.
2. **Show commands/help**: On launch, display or provide instructions for available commands.
3. **Input loop**: Prompt user to enter a command.
4. **Dispatch command**:
    - `book_open`: Prompt for book name, show page count if found.
    - `book_add`: Prompt for name and page number, add new entry.
    - `edit_book`: Prompt for name and new page, update book.
    - `showall`: List all books.
    - `backup`: Backup current data file.
    - `restore`: Restore from backup file.
    - `help`: Re-display this list.
    - `exit`: End session.
5. **Persist changes**: On add/edit/restore, write to data file immediately.
6. **Repeat**: Continue until exit command.

All user data and changes are persisted in real time, ensuring no accidental data loss.
