from aiokeitaro.api import API
from aiokeitaro.utils import remove_key_values

class Domain(API):

    def __init__(self, client, endpoint='domains'):
        super(Domain, self).__init__(client, endpoint)

    async def get(self, domain_id=None):
        """
        Gets list of domains or specific one
        """
        return await super(Domain, self).get(domain_id)

    async def get_deleted(self):
        """
        Gets all deleted domains
        """
        return await super(Domain, self).get('deleted')

    async def create(self, name, *, default_campaign_id=None, wildcard=None,
               catch_not_found=None, notes=None, ssl_redirect=None,
               allow_indexing=None):
        """
        Creates new domain with
        """
        return await super(Domain, self).post(**remove_key_values(locals()))

    async def check(self, domain_id):
        """
        Updates domain status
        """
        return await super(Domain, self).post(domain_id, 'check')

    async def restore(self, domain_id):
        """
        Restores domain by its id from archive
        """
        return await super(Domain, self).post(domain_id, 'restore')

    async def update(self, domain_id, *, name=None, is_ssl=None,
               default_campaign_id=None, state=None, wildcard=None,
               catch_not_found=None, notes=None):
        """
        Updates domain name by id
        """
        return await super(Domain, self).put(
            domain_id, **remove_key_values(locals()))
