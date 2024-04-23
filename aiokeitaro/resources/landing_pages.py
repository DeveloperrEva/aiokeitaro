from aiokeitaro.api import API
from aiokeitaro.utils import remove_key_values

class Landing(API):

    def __init__(self, client, endpoint='landing_pages'):
        super(Landing, self).__init__(client, endpoint)

    async def get(self, landing_id=None):
        """
        Gets all landing pages or specific one by its id
        """
        return await super(Landing, self).get(landing_id)

    async def download(self, landing_id: int):
        """
        Downloads landing
        """
        return await super(Landing, self).get(landing_id, 'download')

    async def get_file(self, landing_id, file_path):
        """
        Gets file data of local landing
        """
        return await super(Landing, self).get(landing_id, 'get_file', path=file_path)

    async def get_structure(self, landing_id):
        """
        Gets file structure of local landing
        """
        return await super(Landing, self).get(landing_id, 'get_structure')

    async def create(self, name, *, action_payload=None, group_id=None, state=None,
               landing_type=None, action_type=None, url=None, archive=None):
        """
        Creates new landing page
        """
        return await super(Landing, self).post(**remove_key_values(locals()))

    async def add_file(self, landing_id, file_path):
        """
        Adds file to a landing page with landing_id
        """
        return await super(Landing, self).post(landing_id, 'add_file')

    async def clone(self, landing_id):
        """
        Clones landing page by its landing_id
        """
        return await super(Landing, self).post(landing_id, 'clone')