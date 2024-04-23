from aiokeitaro.api import API
from aiokeitaro.utils import remove_key_values

class Integration(API):

    def __init__(self, client, endpoint='integrations'):
        super(Integration, self).__init__(client, endpoint)

    async def avscan(self):
        """
        Returns AVScan key
        """
        return await super(Integration, self).get('avscan')

    async def avscan_update(self, avscan_key):
        """
        Updates AVScan key
        """
        return await super(Integration, self).put('avscan', avscan_key=avscan_key)

    async def facebook(self, integration_id=None):
        """
        Returns Facebook all facebook integrations or specific one by integration_id
        """
        return await super(Integration, self).get('facebook', integration_id)

    async def facebook_update(self, integration_id, name=None, ad_account_id=None,
                        token=None, proxy_enabled=None, proxy=None):
        """
        Updates facebook integration
        """
        return await super(Integration, self).put(
            'facebook', **remove_key_values(locals()))

    async def facebook_campaigns(self, integration_id):
        """
        Returns campaigns link to facebook integration
        """
        return await super(Integration, self).get(
            'facebook', facebook_id, 'campaign')

    async def imklo(self):
        """
        Returns IMKLO url
        """
        return await super(Integration, self).get('imklo')

    async def imklo_update(self, imklo_api_url):
        """
        Updates IMKLO api url
        """
        return await super(Integration, self).put(
            'imklo', imklo_api_url=imklo_api_url)

    async def facebook_create(self, name, ad_account_id, token, proxy_enabled, proxy):
        """
        Creates facebook integration
        """
        return await super(Integration, self).post(
            'facebook', **remove_key_values(locals()))

    async def facebook_add_campaign(self, integration_id, campaign_id):
        """
        Adds campaign to facebook integration
        """
        return await super(Integration, self).post(
            'facebook', integration_id, 'campaign')
