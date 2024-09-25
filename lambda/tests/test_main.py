from src.main import lambda_handler


class TestMain:

    def test_lambda_handler_should_return_ok(self, event):
        result = lambda_handler(event, None)

        assert result["statusCode"] == 200

    def test_lambda_handler_should_return_forbidden(self, event):
        event["headers"].update({"documentNumber": "111"})
        result = lambda_handler(event, None)

        assert result["statusCode"] == 401
