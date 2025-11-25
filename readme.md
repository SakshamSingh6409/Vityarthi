# Book Management System

A Python-based command-line application for managing a personal book library with features to track, organize, and manage books with persistent data storage.

## Overview

The Book Management System is an interactive console application designed to help users maintain a collection of books they are reading or have read. Users can track books by name and current page number, with all data automatically persisted to JSON files. The application provides an intuitive interface for managing multiple books and includes backup/restore functionality for data safety.

## Features

- Add new books and their current page number
- Edit the page number of existing books
- View all books at a glance
- Open a book to see its last read page
- Backup and restore your book database with a single command
- Command-line interface with helpful prompts
- Modular code structure (CLI, Logic, Storage)

### Core Functionality
- **Open Book**: View all books in the library and check the current page number of a selected book
- **Add Book**: Add new books to the collection with initial page number tracking
- **Edit Book**: Update the page number for any existing book to track reading progress
- **Show All Books**: Display a complete list of all books currently in the library

### Data Management
- **Data Persistence**: All book data is automatically saved to `data.json` in JSON format
- **Backup & Restore**: Create backup copies of book data (`data_backup.json`) and restore from backups if needed
- **Automatic Error Recovery**: Handles missing files gracefully with fallback mechanisms

### User Interface
- **Interactive Menu**: Command-based interface with intuitive prompts
- **Command System**: Advanced users can use command mode for faster operations
- **Help System**: Built-in help command showing all available operations
- **Input Validation**: Error handling for invalid book names and incorrect inputs

## Technologies & Tools Used

- **Language**: Python 3.x
- **Data Storage**: JSON (JavaScript Object Notation)
- **Development Environment**: Command-line / Terminal
- **File I/O**: Native Python file handling
- **Data Format**: Lightweight JSON for portability and simplicity

## Installation & Setup

### Prerequisites
- Python 3.6 or higher installed on your system
- Basic terminal/command prompt access

### Steps to Install & Run

1. **Download the Project**
   ```bash
   git clone <repository-url>
   cd book-management-system
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **Run the Application**
   ```bash
   python main.py
   # or
   python3 main.py
   ```

4. **Follow the On-Screen Prompts**
   - Start with "yes" or "no" to begin reading a book
   - Use available commands: `book_open`, `book_add`, `edit_book`, `showall`, `backup`, `restore`, `help`
   - Type "stop" or "exit" to terminate the application

## Usage Examples

### Adding a Book
```
Do you want to read a book(yes/no): yes
- [existing books will be shown]
Enter book name: Harry Potter
Enter page no.: 150
```

### Editing Book Progress
```
Do you want to read a book(yes/no): no
Do you want to add or edit a book(add/edit): edit
- [books will be displayed]
Enter book name: Harry Potter
Enter new page no.: 175
```

### Using Commands
```
Do you want to read a book(yes/no): yes
[Enter command mode]
Enter command: showall
- Harry Potter
- The Hobbit
Enter command: backup
```

## Project Structure

```
book-management-system/
├── main.py                 # Main application file with all functions
├── data.json              # Current book database (auto-created)
├── data_backup.json       # Backup copy of book data (auto-created)
├── README.md              # Project documentation
└── statement.md           # Problem statement and requirements
```

## Instructions for Testing

### Manual Testing Scenarios

1. **Test Adding Books**
   - Run the program
   - Select "no" when asked if you want to read a book
   - Choose "add" to add a new book
   - Enter book name and page number
   - Verify the book appears when you view all books

2. **Test Editing Books**
   - Add a test book (e.g., "Test Book - 50 pages")
   - Choose "edit" option
   - Select the test book and update the page number to 75
   - Verify the update is reflected in the book list

3. **Test Data Persistence**
   - Add several books and exit the program
   - Run the program again
   - Verify all previously added books are still present

4. **Test Backup & Restore**
   - Add test books and use the "backup" command
   - Verify `data_backup.json` file is created
   - Use the "restore" command
   - Confirm data is restored correctly

5. **Test Invalid Input Handling**
   - Try entering a book name that doesn't exist when opening/editing
   - Try invalid commands
   - Verify appropriate error messages are shown

6. **Test Help System**
   - Enter command mode by selecting "commands"
   - Type "help" to view all available commands
   - Verify all commands are listed with descriptions

## Data Format

Book data is stored in JSON format:
```json
[
  {
    "Name": "Book Title",
    "Page": 123
  },
  {
    "Name": "Another Book",
    "Page": 45
  }
]
```

## Key Implementation Details

- **Modular Functions**: Each feature is implemented as a separate function for maintainability
- **Dictionary-Based Command Mapping**: Commands are mapped to functions using Python dictionaries for extensibility
- **File Error Handling**: Graceful handling of missing or corrupted JSON files
- **Recursive Functions**: Open book function recursively handles invalid entries
- **Lambda Functions**: Used in command mapping for flexible function execution

## Known Limitations

- Single user only (no multi-user support)
- No book metadata beyond name and page number
- Page number tracking is manual (no reading time estimation)
- No search or filtering capabilities
- Console-based interface only (no GUI)

## Future Enhancements

- Add book metadata (author, ISBN, publication date, genre)
- Implement search and filtering functionality
- Add reading statistics and progress tracking
- Create a graphical user interface (GUI)
- Add user account management for multi-user support
- Implement book ratings and reviews
- Add book recommendations based on reading history
- Support for multiple categories/shelves

## Testing & Validation

All core functions have been tested for:
- ✓ Correct file I/O operations
- ✓ JSON serialization/deserialization
- ✓ Error handling for missing books
- ✓ Data persistence across sessions
- ✓ Backup and restore functionality
- ✓ User input validation

## Screenshots

[Screenshots showing the program interface and sample operations would be included here during deployment]

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes with clear commit messages
4. Submit a pull request

## License

This project is provided as-is for educational purposes.

## Author

Student Project - VITyarthi Build Your Own Project Initiative

## Support

For issues or questions about the application:
- Check the help system by typing "help" in command mode
- Review the statement.md file for project requirements
- Consult the detailed project report for implementation details

---

**Last Updated**: November 2025
**Version**: 1.0
