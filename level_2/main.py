from level_1.main import get_cleaned_data_pipeline
from level_2.ingestion import dict_to_obj, injest_logs
from level_2.schema import Base
from level_2.connection import get_engine

def main():
    dir_path = "applications"
    # create schema if not exist
    Base.metadata.drop_all(get_engine())
    Base.metadata.create_all(get_engine())
    
    # data injestion pipeline
    data = get_cleaned_data_pipeline(dir_path)
    data = dict_to_obj(data)
    injest_logs(data)


if __name__ == "__main__":
    main()
