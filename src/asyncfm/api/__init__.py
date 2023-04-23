import aiohttp
from typing import Optional, Dict
from lastfm.api.user import LastFMUser
from lastfm.exceptions import get_error


FM = type["LastFMAPI"]


class LastFMAPI:
    def __init__(
        self,
        api_key: str,
        session: "Optional[aiohttp.ClientSession]" = None,
    ):
        self.api_key = api_key
        self.base_url = "http://ws.audioscrobbler.com/2.0/"
        self.user = LastFMUser(api=self)
        self.session = session

    async def _request(self, session: "aiohttp.ClientSession", params: Dict[str, str]):
        async with session.get(url=self.base_url, params=params) as response:
            if response.status == 200:
                return await response.json()

            error_data = await response.json()

            raise (get_error(int(error_data.get("error"))))(
                int(error_data.get("error")), error_data.get("message", "")
            )

    async def _make_request(self, params: Dict[str, str]) -> Optional[Dict]:
        params = {"api_key": self.api_key, "format": "json", **params}

        if self.session is None:
            async with aiohttp.ClientSession() as session:
                return await self._request(session=session, params=params)

        return await self._request(session=self.session, params=params)
