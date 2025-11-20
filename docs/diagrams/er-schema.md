# ER/Schema Design

**Entity: Book**
- Name: string (book identifier, unique)
- Page: integer (last page/read page)

**Relationships:** None required (flat list)

**Storage:**  
- Main data file: `data/data.json`
- Backup:        `data/data_backup.json`
- Both files are lists of `{"Name": ..., "Page": ...}` objects in JSON.

**Example:**
[
{"Name": "book1", "Page": 234},
{"Name": "book2", "Page": 150}
]