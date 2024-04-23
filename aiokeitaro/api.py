import json

class API:
    def __init__(self, client, resource_path):
        self.client = client
        self.resource_path = resource_path

    @staticmethod
    def build_url(*path_params) -> str:
        """
        Builds URL path separated with slashes
        """
        return '/'.join(str(par).rstrip('/') for par in path_params if par)

    def _query_params_remove_none_values(self, query_params: dict) -> dict:
        """
        Removes None keys and values from query parameters(payload)
        """
        return {key: val for key, val in query_params.items() if val}

    def _build_payload(self, query_params: dict) -> dict:
        """
        Builds and validates request payload
        """
        return self._query_params_remove_none_values(query_params)

    async def prepare_request(self, method, *path_params, **query_params):
        """
        Preparing http request for api call: building endpoint and payload
        """
        endpoint = API.build_url(self.resource_path, *path_params)
        payload = self._build_payload(query_params)
        
        response = await self.client.send_request(
            method, endpoint, data=json.dumps(payload))
        
        return response

    async def get(self, *path_params, **query_params):
        return await self.prepare_request('GET', *path_params, **query_params)

    async def post(self, *path_params, **query_params):
        return await self.prepare_request('POST', *path_params, **query_params)

    async def put(self, *path_params, **query_params):
        return await self.prepare_request('PUT', *path_params, **query_params)

    async def delete(self, *path_params, **query_params):
        return await self.prepare_request('DELETE', *path_params, **query_params)
