from pathlib import Path
import json

def store_logs(file_path: Path|str, logs: list[dict]):
    """
    Store logs in json format.
    """
    if isinstance(file_path, str):
        file_path = Path(file_path)

    dir_path = file_path.parent
    # create dir if doesn't exist
    dir_path.mkdir(parents=True, exist_ok=True)

    with file_path.open('w') as f:
        json.dump(logs, f, indent=4)