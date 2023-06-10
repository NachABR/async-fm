import aiohttp
from typing import Optional, Dict
from asyncfm.api.user import LastFMUser
from asyncfm.exceptions import get_error


class LastFMAPI:
    def __init__(
        self,
        api_key: str,
        session: "Optional[aiohttp.ClientSession]" = None,
    ):
        self.api_key = api_key
        self.base_url = "http://ws.audioscrobbler.com/2.0/"
        self.session = session

        self.user = LastFMUser(api=self)

    async def _request(self, session: "aiohttp.ClientSession", params: Dict[str, str]):
        async with session.get(url=self.base_url, params=params) as response:
            data = await response.json()
            if response.status == 200:
                return data

            error_code, error_message = data.get("error"), data.get("message")

            raise get_error(code=error_code)(code=error_code, message=error_message)

    async def _make_request(self, params: Dict[str, str]) -> Optional[Dict]:
        params = {"api_key": self.api_key, "format": "json", **params}

        if self.session is None:
            async with aiohttp.ClientSession() as session:
                return await self._request(session=session, params=params)

        return await self._request(session=self.session, params=params)
