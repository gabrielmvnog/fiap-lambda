from src.main import lambda_handler


class TestMain:
    def test_should_receive_event_success(self, event):
        lambda_handler(event, None)
