import sys
from pathlib import Path

# Repo root is one level above tests/, and src/ sits at the repo root.
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))
