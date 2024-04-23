from aiokeitaro.api import API


class Log(API):

    def __init__(self, client, endpoint='logs'):
        super(Log, self).__init__(client, endpoint)

    async def get(self, logs_type, limit, offset=None, query=None):
        """
        Gets logs logs
        """
        return await super(Log, self).get(logs_type, limit=limit, offset=offset, query=query)

    async def types(self):
        """
        Getting logs types
        """
        return await super(Log, self).get('types')
