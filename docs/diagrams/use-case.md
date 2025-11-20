# Use Case Diagram (Textual)

**Actor**: User

**Use Cases:**
- Open Book (View page number for a given book)
- Add Book (Add new book and page count)
- Edit Book (Update page number for an existing book)
- Show All (List all books)
- Backup Data (Save data to a backup file)
- Restore Data (Restore books from a backup file)
- Help (Show all available commands)
- Exit (Terminate session)

**Flow**:  
User → CLI → (Books Logic & Storage) → JSON File(s)
