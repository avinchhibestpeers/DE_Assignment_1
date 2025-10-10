from pathlib import Path
from tqdm import tqdm

def get_log(file_path: Path|str) -> str:
    """
    Returns log extracted from give file path.
    """
    if isinstance(file_path, str):
        file_path = Path(file_path)

    if not file_path.exists():
        print(f"WARNING: File {file_path} not found")
        return ""

    with file_path.open('r') as f:
        data = f.read()
    
    return data.strip()

def get_all_logs(dir_path: str) -> list[str]:
    """
    Returns logs from log files in dir_path directory.
    """
    dir_path_name = Path(dir_path)
    if not dir_path_name.exists():
        raise FileNotFoundError(f"Directory {dir_path} not found")
    logs = []
    for file_path in tqdm(dir_path_name.iterdir(), desc="Loading files: "):
        log = get_log(file_path)
        if len(log) != 0:
            logs.append(log)
    
    return logs