from pytest import fixture
from testcontainers.postgres import PostgresContainer


@fixture
def event():
    return {"documentNumber": "documentNumber", "password": "password"}


@fixture
def postgre_container(monkeypatch):
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

        yield
