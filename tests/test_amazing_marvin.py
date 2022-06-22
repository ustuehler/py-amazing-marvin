import unittest
from datetime import date

# noinspection PyUnresolvedReferences
from amazing_marvin import AmazingMarvinAPI, API_URL


class MockResponse:
    def __init__(self, content: str):
        self.content = content

    def raise_for_status(self) -> None:
        pass


class MockSession:
    headers: dict = {}

    def __init__(self, path_content: dict[str, str]) -> None:
        self.path_content = path_content

    def get(self, path: str) -> MockResponse:
        return MockResponse(self.path_content[path])


class MockRequestsModule:
    def __init__(self, path_content: dict[str, str]) -> None:
        self.path_content = path_content
        self.Session = lambda: MockSession(self.path_content)


class TestAmazingMarvinAPI(unittest.TestCase):

    def setUp(self) -> None:
        today = date.today()

        self.api = AmazingMarvinAPI(
            api_token='ignored_by_mock_requests_module',
            requests_module=MockRequestsModule({
                f'{API_URL}/me': '{}',
                f'{API_URL}/todayItems?date={today.isoformat()}': '[]'
            })
        )

    def test_me(self):
        self.assertIsInstance(self.api.me(), dict)

    def test_today_items(self):
        self.assertIsInstance(self.api.today_items(), list)


if __name__ == '__main__':
    unittest.main()
