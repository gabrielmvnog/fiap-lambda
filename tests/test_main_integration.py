import pytest

from src.main import database_connection


@pytest.mark.usefixtures("postgre_container")
class TestIntegrationMain:
    def test_should_connect_to_postgres(self):
        connection = database_connection()
        assert connection
