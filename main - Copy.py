#This is a book management program that allows users to read, add, edit books and execute some commands.

import json

from function import *
from variables import *

books = read_file()

def handle_yes(books):
    open_book(books)

def handle_no(books):
    a = input("Do you want to add or edit a book(add/edit) : ").strip().lower()
    if a in actions_no:
        actions_no[a](books)
    else:
        print("Invalid input")

def handle_commands(books):
    command_run = True
    while command_run:
        command = input("Enter command: ")
        command(command, books)

def handle_exit(books):
    run = False

actions_no = {
    "add": add_book,
    "edit": edit_book
}
actions = {
    "yes": handle_yes,
    "no": handle_no,
    "commands": handle_commands,
    "command": handle_commands,
    "exit": handle_exit,
    "stop": handle_exit
}

while run:
    e = input("Do you want to read a book(yes/no): ").strip().lower()
    action = actions.get(e, lambda books: print("Invalid Input"))
    action(books)
    if run == True:
        cont = input("Do you want to continue(yes/no): ").strip().lower()
        if cont == "no":
            run = False
        elif cont == "yes":
            continue
        else:
            print("Invalid Input")
