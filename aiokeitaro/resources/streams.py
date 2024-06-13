from aiokeitaro.api import API
from aiokeitaro.utils import remove_key_values, set_resource_default_fields


class Stream(API):

    def __init__(self, client, endpoint='streams'):
        self.client = client
        super(Stream, self).__init__(client, endpoint)

    async def get(self, stream_id):
        """
        Gets stream by its id
        """
        return await super(Stream, self).get(stream_id)

    async def get_deleted(self):
        """
        Gets all deleted streams
        """
        return await super(Stream, self).get('deleted')

    async def search(self, query):
        """
        Gets stream by word in payload stream
        """
        return await super(Stream, self).get('search', query=query)

    async def get_schemas(self):
        """
        Gets available stream schemas
        """
        return await self.client.send_request('GET', 'stream_schemas')

    async def get_types(self):
        """
        Gets avaiable stream types
        """
        return await self.client.send_request('GET', 'stream_types')

    async def get_actions(self):
        """
        Getting stream actions
        """
        return await self.client.send_request('GET', 'stream_actions')

    async def create(self, *, campaign_id, name, type, action_type, schema,
               position=None, weigth=None, action_options=None, comments=None,
               state=None, collect_clicks=None, filter_or=None, filters=None,
               triggers=None, landings=None, offers=None):
        """
        Creates new stream for campaign with campaign id.
        To retrieve available stream schemas use get_schemas(),
        to retrieve available stream action types use get_actions()
        """
        return await super(Stream, self).post(**remove_key_values(locals()))

    async def disable(self, stream_id):
        """
        Changes stream state to disabled
        """
        return await super(Stream, self).post(stream_id, 'disable')

    async def enable(self, stream_id):
        """
        Changes stream state to enabled
        """
        return await super(Stream, self).post(stream_id, 'enable')

    async def restore(self, stream_id):
        """
        Restores stream from archive
        """
        return await super(Stream, self).post(stream_id, 'restore')

    async def update(self, stream_id, *, campaign_id, name=None, type=None,
               action_type=None, action_payload=None, schema=None, position=None, weigth=None,
               action_options=None, comments=None, state=None,
               collect_clicks=None, filter_or=None, filters=None,
               triggers=None, landings=None, offers=None):
        """
        Updates stream data by stream_id in campaign with campaign_id
        """
        
        query_params = remove_key_values(locals())
        streams = await self.get(stream_id).json()
        set_resource_default_fields(
            {'action_type': action_type, 'schema': schema},
            query_params, streams)
        return await super(Stream, self).post(**query_params)