import json
from pathlib import Path
from config import DATA_FILE, BACKUP_FILE

def read_data(path: Path = DATA_FILE) -> list:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def write_data(data: list, path: Path = DATA_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def backup(src: Path = DATA_FILE, dest: Path = BACKUP_FILE) -> None:
    data = read_data(src)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def restore(src: Path = BACKUP_FILE, dest: Path = DATA_FILE) -> bool:
    try:
        with src.open("r", encoding="utf-8") as f:
            data = json.load(f)
        write_data(data, dest)
        return True
    except (FileNotFoundError, json.JSONDecodeError):
        return False
