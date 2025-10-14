from level_1.get_logs import get_all_logs
from level_1.clean_logs import clean_all_logs


def get_cleaned_data_pipeline(dir_path: str = "applications") -> list[dict]:
    """
    Data pipeline to get data from logs files, clean and return in list of dict.
    """
    raw_logs = get_all_logs(dir_path)
    cleaned_logs = clean_all_logs(raw_logs)
    return cleaned_logs
