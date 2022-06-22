"""Basic API client for Amazing Marvin."""

import json
from datetime import date, datetime

API_URL = 'https://serv.amazingmarvin.com/api'


class AmazingMarvinAPI:
    """Basic API client for Amazing Marvin implementing methods for at least a
    subset of the endpoints mentioned in the `wiki
    <https://github.com/amazingmarvin/MarvinAPI/wiki/Marvin-API>`_.
    """

    def __init__(self, api_token: str, requests_module=None):
        """Construct a new API client for Amazing Marvin, using the given API
        token to authenticate as a particular user, and the given ``requests``
        module.

        :param api_token: The secret API token of an Amazing Marvin account.

        :param requests_module: A compatible implementation of
          the :mod:`requests` module providing at least
          a compatible :class:`requests.Session` implementation. The default
          implementation will be used if this parameter is ``None``.
        """
        if requests_module is None:
            import requests
            requests_module = requests

        self._session = requests_module.Session()
        self._session.headers['X-API-Token'] = api_token

    def today_items(
            self, today: date or datetime or None = None
    ) -> list[dict[str, any]]:
        """Get tasks and projects scheduled today, including
        rollover/auto-schedule due items, if enabled.

        Note that the Amazing Marvin servers run in the UTC+0 timezone and will
        assume that all dates are in the server's local time zone as well. This
        means that the server has no idea what the user's actual local time zone
        is and will interpret all dates as local to the server.

        :param today: The date or date and time which marks "today" or "now"
        in the user's local timezone. For example, ``datetime.now()`, which is
        also the default value if this parameter is set to ``None``.

        See the `documentation <https://github.com/amazingmarvin/MarvinAPI/wiki/Marvin-API#get-tasks-and-projects-scheduled-today-including-rolloverauto-schedule-due-items-if-enabled>`_
        for more information.
        """
        if today is None:
            today = datetime.now()

        if isinstance(today, datetime):
            today = today.date()

        query = f'date={today.isoformat()}'
        return self._get_json_response_data(f'/todayItems?{query}')

    def me(self) -> dict[str, any]:
        """Retrieve some information about your account.

        See the `documentation <https://github.com/amazingmarvin/MarvinAPI/wiki/Marvin-API#me>`_
        for more information.
        """
        return self._get_json_response_data('/me')

    def _get_json_response_data(self, path: str) -> any:
        response = self._session.get(f"{API_URL}{path}")
        response.raise_for_status()

        data = json.loads(response.content)
        return data
