import aiohttp
from typing import Any, Optional, Dict
from ..api.user import LastFMUser
from ..exceptions import get_error


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
        
    async def get_session(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()
        return self.session
        
    async def __aenter__(self):
        await self.get_session()
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session and not self.session.closed:
            await self.session.close()
    
    async def _make_request(self, params: Dict[str, str]) -> Optional[Dict[str, Any]]:
        params = {"api_key": self.api_key, "format": "json", **params}
        session = await self.get_session()

        async with session.get(url=self.base_url, params=params) as response:
            data: dict = await response.json()
            if response.status == 200:
                return data

            error_code, error_message = data.get("error"), data.get("message")

            raise get_error(code=error_code)(code=error_code, message=error_message)