from src.main import lambda_handler
import pytest
from unittest.mock import patch, MagicMock
from src.main import database_connection, find_user
from sqlalchemy.exc import NoResultFound


@pytest.mark.usefixtures("postgres_client", "db_valida_user")
class TestMain:

    def test_lambda_handler_should_return_true(self, event):
        with patch("src.main.database_connection", return_value=MagicMock()):
            result = lambda_handler(event, None)

            assert result

    def test_lambda_handler_should_return_false(self, event):
        with patch(
            "src.main.database_connection",
            return_value=MagicMock(
                __enter__=MagicMock(
                    return_value=MagicMock(
                        execute=MagicMock(
                            return_value=MagicMock(
                                scalar_one=MagicMock(side_effect=NoResultFound)
                            )
                        )
                    )
                )
            ),
        ):
            event.update({"password": "111"})
            result = lambda_handler(event, None)

            assert not result

    def test_should_connect_to_postgres(self):
        connection = database_connection()

        assert connection

    def test_find_user_should_return_none(self, postgres_session):
        user = find_user(postgres_session, "123", "456")

        assert user is None

    def test_find_user(self, postgres_session, db_valida_user):
        user = find_user(
            postgres_session, db_valida_user.document_number, db_valida_user.password
        )

        assert user.document_number == db_valida_user.document_number
