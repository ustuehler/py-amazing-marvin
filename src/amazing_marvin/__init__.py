import json

import requests as requests

API_URL = 'https://serv.amazingmarvin.com/api'


class AmazingMarvinAPI:
    def __init__(self, api_token: str):
        self._session = requests.Session()
        self._session.headers['X-API-Token'] = api_token

    def me(self) -> dict[str, any]:
        return self._get_json_response_data('/me')

    def _get_json_response_data(self, path: str) -> any:
        response = self._session.get(f"{API_URL}{path}")
        response.raise_for_status()

        data = json.loads(response.content)
        return data
