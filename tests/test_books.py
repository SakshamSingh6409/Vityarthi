from books import *

def test_add_and_open():
    books = []
    add_book(books, "book1", 123)
    assert open_book(books, "book1") == 123

def test_edit_book_found_and_missing():
    books = [{"Name": "b", "Page": 1}]
    assert edit_book(books, "b", 9) is True
    assert books[0]["Page"] == 9
    assert edit_book(books, "x", 5) is False
