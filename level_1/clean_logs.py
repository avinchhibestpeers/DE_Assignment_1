from tqdm import tqdm
import json


def get_dict_value(input: str) -> dict:
    """
    Takes string in json format convert it into dict
    """
    input = input.replace("'", '"')  # replace single quote with double
    proc_input = json.loads(input)
    return proc_input


def clean_log(log: str) -> dict:
    """
    Extract all key values from log string and return cleaned data.
    """
    items = log.split("|")

    cleaned_log = {}

    for item in items:
        key, value = item.split("=")

        key, value = key.strip(), value.strip()

        # if json format make it dict
        if value.startswith("{") and value.endswith("}"):
            value = get_dict_value(value)

        cleaned_log[key] = value

    return cleaned_log


def clean_all_logs(raw_logs: list[str]) -> list[dict]:
    """
    Takes list of raw logs and returns cleaned logs
    """
    cleaned_logs = []

    for log in tqdm(raw_logs, desc="Cleaning files: "):
        cleaned_log = clean_log(log)
        cleaned_logs.append(cleaned_log)

    return cleaned_logs
