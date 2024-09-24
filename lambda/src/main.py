import os
import sqlalchemy
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    document_number = Column(String)
    password = Column(String)


def lambda_handler(event, context) -> bool:
    document_number = event["documentNumber"]
    password = event["password"]

    with database_connection() as session:
        return find_user(session, document_number, password)


def database_connection():
    DB_HOST = os.environ["DB_HOST"]
    DB_USER = os.environ["DB_USER"]
    DB_TABLE = os.environ["DB_TABLE"]
    DB_PASS = os.environ["DB_PASS"]

    engine = sqlalchemy.create_engine(
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_TABLE}"
    )

    return Session(engine)


def find_user(session, document_number, password):
    stmt = (
        select(User)
        .where(User.document_number == document_number)
        .where(User.password == password)
    )

    try:
        user = session.execute(stmt).scalar_one()
    except NoResultFound:
        return None

    return user
