import json
from variables import *

#Function to read and load data from JSON file
def read_file():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except(FileNotFoundError): #json.decoder.LSONDecoderError
        data = []
    return data

#Function to update JSON file with new data
def update_file(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

#Function to restore data from backup JSON file
def restore():
    try:
        with open("data_backup.json", "r") as file:
            data = json.load(file)
        update_file(data)
        print("Data restored successfully from backup.")
    except(FileNotFoundError):
        print("Backup file not found.")

#Function to backup data to another JSON file
def backup(books):
    with open("data_backup.json", "w") as file:
        json.dump(books, file)

#Function to open a book and display its page number
def open_book(loaded_books):
    show_all(loaded_books)
    book=input("Enter book name: ")
    for i in loaded_books:
        if i["Name"]==book:
            print(f'Page of the book is: {i["Page"]}')
            break
    else:
        print("Book not found")
        open_book(loaded_books)             

#Function to edit a book's page number
def edit_book(loaded_books):
    show_all(loaded_books)
    z=False
    book = input("Enter book name: ")
    for i in loaded_books:
        if i["Name"]==book:
            page=int(input("Enter new page no.: "))
            i["Page"]=page
            z=True
            break
    if z==False:
        print("Book not found")
    update_file(loaded_books)

#Function to add a new book
def add_book(loaded_books):
    book = input("Enter book name: ")
    page=int(input("Enter page no.: "))
    book_new = {"Name": book, "Page": page}
    loaded_books.append(book_new)
    update_file(loaded_books)

#Function to show all books
def show_all(loaded_books):
    print(loaded_books)

def stop():
    run = False

def exit():
    command_run = False

def help():
    print("""book_open - Open a book
book_add - Add a new book
edit_book - Edit a book's page number
showall - Show all books
backup - Backup data to another file
stop - Stop the program
restore - Restore data from backup file
help - Show this help message""")
    

command_actions = {
    "book_open": open_book,
    "book_add": add_book,
    "edit_book": edit_book,
    "showall": show_all,
    "backup": lambda books: backup(books),
    "restore": lambda books: restore(),  # if restore works on files directly
    "stop": lambda books: stop(),
    "exit": lambda boos: exit(),
    "help": lambda books: help()
}

def command(x, books):
    action = command_actions.get(x.lower())
    if action:
        action(books)
    else:
        print("Invalid command")