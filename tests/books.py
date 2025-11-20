from typing import List, Dict, Optional

Book = Dict[str, int | str]

def show_all(books: List[Book]) -> str:
    if not books:
        return "No books available."
    return "\n".join(f"- {b.get('Name','?')} (Page: {b.get('Page','?')})" for b in books)

def _find_index(books: List[Book], name: str) -> Optional[int]:
    for i, b in enumerate(books):
        if str(b.get("Name","")).strip().lower() == name.strip().lower():
            return i
    return None

def open_book(books: List[Book], name: str) -> Optional[int]:
    idx = _find_index(books, name)
    if idx is None:
        return None
    try:
        return int(books[idx].get("Page"))
    except (TypeError, ValueError):
        return None

def add_book(books: List[Book], name: str, page: int) -> None:
    books.append({"Name": name, "Page": int(page)})

def edit_book(books: List[Book], name: str, new_page: int) -> bool:
    idx = _find_index(books, name)
    if idx is None:
        return False
    books[idx]["Page"] = int(new_page)
    return True
