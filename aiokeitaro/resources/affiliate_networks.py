from aiokeitaro.api import API
from aiokeitaro.utils import remove_key_values

class Affiliate(API):
    def __init__(self, client, endpoint='affiliate_networks'):
        super(Affiliate, self).__init__(client, endpoint)

    async def get(self, affiliate_network_id=None):
        """
        Gets all affiliate networks or specific one by its id
        """
        return await super(Affiliate, self).get(affiliate_network_id)

    async def create(self, name, *, postback_url=None, offer_param=None, offers=None,
               template_name=None, notes=None, pull_api_options=None,
               state=None):
        """
        Creates new affiliate network
        """
        return await super(Affiliate, self).post(
            *remove_key_values(locals()))

    async def clone(self, affiliate_network_id):
        """
        Clones affiliate network by id
        """
        return await super(Affiliate, self).post(
            affiliate_network_id, 'clone')

    async def update(self, affiliate_network_id, name=None, postback_url=None):
        """
        Updates affiliate network
        """
        return await super(Affiliate, self).put(
            affiliate_network_id, name=name, postback_url=postback_url)

