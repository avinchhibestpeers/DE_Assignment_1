from datetime import datetime
from sqlalchemy.orm import Session

from level_2.schema import Logs
from level_2.connection import get_engine


def dict_to_obj(data: list[dict]) -> list[Logs]:
    """
    Converts Dictionary format data into ORM objects.
    """
    rows = [
        Logs(
            id=log["id"],
            therapeutic_area=log["therapeutic_area"],
            created_at=datetime.strptime(log["created_at"], "%Y-%m-%d %H:%M:%S"),
            site_name=log['site']["site_name"],
            site_category=log['site']['site_category']
        ) 
        for log in data
    ]
    return rows

def injest_logs(data: list[Logs]):
    """
    Injest logs to sql database.
    """
    engine = get_engine()
    with Session(engine) as session:
        session.add_all(data)
        session.commit()