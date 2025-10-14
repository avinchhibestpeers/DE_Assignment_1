from functools import cache

from sqlalchemy import create_engine

@cache
def get_engine():
    connection_str="mysql+pymysql://admin:admin@localhost:3306/default?charset=utf8mb4"
    engine = create_engine(connection_str, echo=True, pool_pre_ping=True)
    return engine
    # with engine.connect() as conn:
    #     result = conn.execute(text("select 'hello world'"))
    #     print(result.all())
    