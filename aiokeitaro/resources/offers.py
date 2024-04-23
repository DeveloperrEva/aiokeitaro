from aiokeitaro.api import API
from aiokeitaro.utils import remove_key_values

class Offer(API):

    def __init__(self, client, endpoint='offers'):
        super(Offer, self).__init__(client, endpoint)

    async def get(self, offer_id=None):
        """
        Gets all offers or specific one by its id
        """
        return await super(Offer, self).get(offer_id)

    async def download_landing(self, offer_id):
        """
        Downloads local landing
        """
        return await super(Offer, self).get(offer_id, 'download')

    async def files_structure(self, offer_id):
        """
        Returns files structure of local landing
        """
        return await super(Offer, self).get(offer_id, 'get_structure')

    async def get_file(self, offer_id, file_path):
        """
        Gets file data of local landing
        """
        return await super(Offer, self).get(offer_id, path=file_path)

    async def create(self, name, *, group_id=None, offer_type=None,
               action_type=None, action_payload=None, archive=None,
               affiliate_network_id=None, payout_value=None, notes=None,
               payout_currency=None, payout_type=None, state=None,
               payout_auto=None, payout_upsell=None, country=None):
        """
        Creates new offer
        """
        return await super(Offer, self).post(**remove_key_values(locals()))

    async def add_file(self, offer_id, file_path):
        """
        Creates file of local landing
        """
        return await super(Offer, self).post(offer_id, 'add_file', path=file_path)

    async def clone(self, offer_id):
        """
        Clones offer by its id
        """
        return await super(Offer, self).post(offer_id, 'clone')