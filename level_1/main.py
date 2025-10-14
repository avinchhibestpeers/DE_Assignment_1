from level_1.pipeline import get_cleaned_data_pipeline
from level_1.store_logs import store_logs
def main():
    dir_path = "applications"

    # pipeline
    cleaned_logs = get_cleaned_data_pipeline(dir_path)
    result_path = "level_1/result/cleaned_logs.json"
    store_logs(result_path, cleaned_logs)
    print(f"Result stored at: {result_path}")



if __name__ == '__main__':
    main()