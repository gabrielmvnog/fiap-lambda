from pytest import fixture


@fixture
def event():
    return {"documentNumber": "documentNumber", "password": "password"}
