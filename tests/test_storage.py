from pathlib import Path
from storage import write_data, read_data, backup, restore

def test_roundtrip_and_backup_restore(tmp_path: Path):
    data_path = tmp_path / "data.json"
    backup_path = tmp_path / "data_backup.json"
    sample = [{"Name": "a", "Page": 2}]

    write_data(sample, data_path)
    assert read_data(data_path) == sample

    backup(data_path, backup_path)
    assert read_data(backup_path) == sample

    write_data([], data_path)
    assert restore(backup_path, data_path) is True
    assert read_data(data_path) == sample
