from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "data.json"
BACKUP_FILE = DATA_DIR / "data_backup.json"
