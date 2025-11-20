# Sequence Diagram (book_open example)

1. User types `book_open`
2. CLI lists all books
3. CLI prompts for book name
4. User enters name (e.g., "Book1")
5. CLI calls `books.open_book(books, "Book1")`
6. Domain logic looks up "Book1" and returns page or None
7. CLI prints result to user
