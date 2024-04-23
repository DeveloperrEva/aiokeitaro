import os
import aiohttp

from .utils import build_host_url
from .api import API
from .resources import Affiliate, Campaign

class Keitaro:
    api_endpoint = 'admin_api/v1/'

    def __init__(self, api_key: str, host: str, from_env: bool = False) -> None:
        if from_env:
            self.api_key = os.environ[api_key]
            self.host = os.environ[host]
        else:
            self.api_key = api_key
            self.host = host

    @property
    def api_key(self):
        return self._api_key

    @property
    def host(self):
        return self._host

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key
    
    @host.setter
    def host(self, host):
        self._host = build_host_url(host)

    async def send_request(self, method: str, endpoint: str, *kwargs):
        """
        Sends HTTP request to Keitaro Admin API
        """
        url = API.build_url(self.host, Keitaro.api_endpoint, endpoint)

        async with aiohttp.ClientSession() as session:
            async with session.request(
                method, url, headers={'Api-Key': self.api_key}, *kwargs
            ) as response:
                data = await response.json()
                return data