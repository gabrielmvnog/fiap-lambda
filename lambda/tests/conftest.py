from pytest import fixture


@fixture
def event():
    return {"headers": {"documentNumber": "12345678910"}}
