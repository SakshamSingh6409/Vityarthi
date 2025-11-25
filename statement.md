# Book Management System - Project Statement

## Problem Statement

Many avid readers and students struggle to keep track of their reading progress across multiple books. Traditional methods like physical bookmarks or notebooks are cumbersome and prone to loss. While many commercial book management applications exist, they often come with unnecessary features, complex interfaces, or require internet connectivity.

**Problem**: Users need a simple, lightweight, and reliable tool to track their book reading progress without the overhead of web-based applications or complex user interfaces. The tool should allow quick access to their reading progress, ability to add new books to their collection, and the peace of mind that their reading data is safely backed up and recoverable.

**Scope**: This project addresses the need for a personal book management system with essential features - add books, track page numbers, edit progress, and backup data - without unnecessary complexity. The system targets individual readers who want a straightforward command-line solution that works offline and stores data locally.

## Project Objectives

1. **Provide Core Book Management**: Enable users to add, edit, and view books in their personal library
2. **Persistent Data Storage**: Automatically save reading progress so data is not lost between sessions
3. **Data Safety**: Implement backup and restore functionality to protect against data loss
4. **User-Friendly Interface**: Create an intuitive command-based menu system accessible to non-technical users
5. **Reliable Error Handling**: Gracefully handle errors and edge cases with appropriate user feedback
6. **Extensibility**: Design the system with modular functions that can be easily extended with new features

## Scope of the Project

### In Scope
- Book CRUD operations (Create, Read, Update operations)
- JSON-based data persistence
- Backup and restore functionality
- Command-line user interface
- Input validation and error handling
- Interactive menu system
- Help documentation

### Out of Scope
- Graphical User Interface (GUI)
- Multi-user support or authentication
- Cloud synchronization
- Advanced book metadata (author, genre, rating, etc.)
- Reading statistics or analytics
- Integration with online book databases
- Mobile application support

## Target Users

1) Students and casual readers who want to track reading progress
2) Educators and reviewers looking for a clean, testable reference project

### Primary Users
- **Casual Readers**: Individuals reading 1-10 books simultaneously who want to track progress
- **Students**: Students reading multiple textbooks and reference materials who need progress tracking
- **Avid Readers**: Book enthusiasts who maintain personal libraries and want organized tracking

### Secondary Users
- **Book Clubs**: Members who need to track individual reading progress for group discussions
- **Educators**: Teachers who want to track student reading progress for assignments

### User Characteristics
- Basic computer literacy required
- Comfortable with command-line interfaces
- Value simplicity over advanced features
- Prefer offline, local storage solutions
- Want quick, lightweight applications

## High-Level Features


### Feature 1: Book Management
**Description**: Users can add new books to their library and track them by name and current page number.
- Add books with initial page tracking
- Store book information in a structured format
- View complete list of all books in the collection

### Feature 2: Progress Tracking
**Description**: Users can monitor their reading progress by editing the page number for any book.
- Update page number for ongoing reads
- View current page number when opening a book
- Track multiple books simultaneously

### Feature 3: Data Persistence
**Description**: All book data is automatically saved and persists between application sessions.
- Automatic JSON file generation and updates
- Load existing data on application startup
- Handle missing or corrupted data gracefully

### Feature 4: Data Protection
**Description**: Users can backup their book data and restore from backups if needed.
- Create backup copies of the entire library
- Restore from backup files in case of data loss
- Error handling if backup files don't exist

### Feature 5: User Interface & Commands
**Description**: Interactive menu-driven interface with command mode for advanced users.
- Main menu with yes/no options for intuitive navigation
- Secondary menu for add/edit operations
- Advanced command mode for power users
- Built-in help system documenting all commands

### Feature 6: Error Handling & Validation
**Description**: Robust error handling and user input validation throughout the application.
- Validate book names before operations
- Handle invalid page number inputs
- Recursive error recovery prompts
- Graceful handling of file system errors

## Functional Requirements

1. **FR1**: The system shall allow users to add a new book with a name and initial page number
2. **FR2**: The system shall allow users to edit the page number of an existing book
3. **FR3**: The system shall display all books in the collection when requested
4. **FR4**: The system shall display the page number of a specific book when selected
5. **FR5**: The system shall persist all book data to a JSON file (data.json)
6. **FR6**: The system shall load all previously saved books when the application starts
7. **FR7**: The system shall create a backup of all book data to a separate JSON file (data_backup.json)
8. **FR8**: The system shall allow users to restore data from the backup file
9. **FR9**: The system shall provide an interactive menu for user operations
10. **FR10**: The system shall provide a command mode with multiple commands for advanced operations
11. **FR11**: The system shall provide a help command that documents all available commands
12. **FR12**: The system shall handle invalid book names by prompting the user to retry

## Non-Functional Requirements

1. **NFR1 - Performance**: The system shall respond to user commands within 1 second for all operations
2. **NFR2 - Reliability**: The system shall maintain data integrity with 99.9% success rate for save operations
3. **NFR3 - Usability**: The system shall be usable by individuals with basic computer skills without external documentation beyond the help command
4. **NFR4 - Data Integrity**: The system shall prevent data loss through automatic saving and backup mechanisms
5. **NFR5 - Error Handling**: The system shall gracefully handle all file I/O errors and invalid user inputs with clear error messages
6. **NFR6 - Maintainability**: The system code shall follow Python best practices with clear function names and comments for maintainability
7. **NFR7 - Compatibility**: The system shall run on Windows, macOS, and Linux operating systems with Python 3.6+
8. **NFR8 - Resource Efficiency**: The system shall use minimal system resources and complete all operations with < 50MB memory footprint

## System Architecture

### Architecture Type
**Simple Modular Architecture** - The application uses a functional programming approach with clear separation of concerns.

### Components

1. **Data Access Layer**
   - `read_file()`: Load book data from JSON
   - `update_file()`: Save book data to JSON
   - `backup()`: Create data backup
   - `restore()`: Recover from backup

2. **Business Logic Layer**
   - `add_book()`: Handle adding new books
   - `edit_book()`: Handle book edits
   - `open_book()`: Handle book selection and viewing

3. **User Interface Layer**
   - Main menu loop with yes/no prompts
   - `handle_yes()`, `handle_no()`: Primary branching
   - `handle_commands()`: Command mode interface

4. **Utility Functions**
   - `show_all()`: Display all books
   - `help()`: Show help information

### Data Flow
```
User Input → Menu Handler → Command/Function → Data Access → File System
                                  ↓
                          Business Logic
                                  ↓
                          User Output
```

## Technology Stack

| Component | Technology |
|-----------|-----------|
| Programming Language | Python 3.x |
| Data Format | JSON |
| Storage | Local File System |
| Interface | Command-Line |
| File I/O | Native Python |

---

**Document Version**: 1.0
**Last Updated**: November 2025
