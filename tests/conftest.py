from pytest import fixture
import sqlalchemy
from testcontainers.postgres import PostgresContainer
from sqlalchemy.orm import Session
from src.main import Base, User


@fixture
def event():
    return {"documentNumber": "123", "password": "123"}


@fixture
def postgres_client(monkeypatch):
    db_user = "test"
    db_pass = "test"
    db_name = "test"

    with PostgresContainer(
        "postgres:16", username=db_user, password=db_pass, dbname=db_name
    ) as postgres:
        psql_url = postgres.get_container_host_ip()

        monkeypatch.setenv("DB_HOST", psql_url)
        monkeypatch.setenv("DB_USER", db_user)
        monkeypatch.setenv("DB_TABLE", db_name)
        monkeypatch.setenv("DB_PASS", db_pass)

        engine = sqlalchemy.create_engine(postgres.get_connection_url())
        Base.metadata.create_all(engine)

        yield engine


@fixture
def postgres_session(postgres_client):
    with Session(postgres_client) as session:
        yield session


@fixture
def db_valida_user(postgres_session):
    user = User(document_number="123", password="123")

    postgres_session.add(user)
    postgres_session.commit()

    return user
