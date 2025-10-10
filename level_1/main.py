from level_1.get_logs import get_all_logs
from level_1.clean_logs import clean_all_logs
from level_1.store_logs import store_logs
def main():
    dir_path = "applications"

    # pipeline
    raw_logs = get_all_logs(dir_path)
    cleaned_logs = clean_all_logs(raw_logs)
    result_path = "level_1/result/cleaned_logs.json"
    store_logs(result_path, cleaned_logs)
    print(f"Result stored at: {result_path}")



if __name__ == '__main__':
    main()