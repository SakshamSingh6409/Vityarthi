from storage import read_data, write_data, backup, restore
from books import show_all, open_book as open_bk, add_book as add_bk, edit_book as edit_bk

HELP_TEXT = """Commands:
  book_open       - Open a book and show its page
  book_add        - Add a new book
  edit_book       - Edit a book's page
  showall         - Show all books
  backup          - Backup data.json to data_backup.json
  restore         - Restore from data_backup.json to data.json
  help            - Show this help
  exit            - Quit the program
"""

def handle_book_open(books):
    print(show_all(books))
    name = input("Enter book name: ").strip()
    page = open_bk(books, name)
    print(f"Page of the book is: {page}" if page is not None else "Book not found")

def handle_book_add(books):
    name = input("Enter book name: ").strip()
    try:
        page = int(input("Enter page no.: ").strip())
    except ValueError:
        print("Invalid page number.")
        return
    add_bk(books, name, page)
    write_data(books)
    print("Book added.")

def handle_edit_book(books):
    print(show_all(books))
    name = input("Enter book name: ").strip()
    try:
        page = int(input("Enter new page no.: ").strip())
    except ValueError:
        print("Invalid page number.")
        return
    if edit_bk(books, name, page):
        write_data(books)
        print("Book updated.")
    else:
        print("Book not found.")

def handle_backup(_books):
    backup()
    print("Backup completed.")

def handle_restore(_books):
    if restore():
        print("Data restored successfully from backup.")
    else:
        print("Backup file not found or invalid.")

COMMANDS = {
    "book_open": handle_book_open,
    "book_add": handle_book_add,
    "edit_book": handle_edit_book,
    "showall": lambda books: print(show_all(books)),
    "backup": handle_backup,
    "restore": handle_restore,
    "help": lambda _books: print(HELP_TEXT),
    "exit": None,
}

def run():
    books = read_data()
    print("Type 'help' for commands.")
    while True:
        cmd = input("Enter command: ").strip().lower()
        if cmd == "exit":
            break
        handler = COMMANDS.get(cmd)
        if handler is None:
            print("Invalid command")
            continue
        handler(books)
