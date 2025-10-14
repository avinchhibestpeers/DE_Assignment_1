from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DateTime
from datetime import datetime

"""
CREATE TABLE application(
   id varchar(100),
   therapeutic_area varchar(10),
   created_at timestamp,
   site_name varchar(50),
   site_category varchar(20)
)
"""


class Base(DeclarativeBase):
    pass


class Logs(Base):
    __tablename__ = "Logs"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    therapeutic_area: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime())
    site_name: Mapped[str] = mapped_column(String(100))
    site_category: Mapped[str] = mapped_column(String(100))
