class AmazingMarvinAPI:
    def __init__(self, api_token: str):
        self._api_token = api_token

    def me(self) -> dict[str, any]:
        return {
            'email': "user@example.com"
        }
