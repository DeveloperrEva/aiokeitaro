import json

from aiokeitaro.api import API
from aiokeitaro.utils import (
    generate_random_string, remove_key_values,
    filter_resource_entities_by_key_value
)

class Campaign(API):

    def __init__(self, client, endpoint='campaigns'):
        super(Campaign, self).__init__(client, endpoint)

    async def get(self, campaign_id=None):
        """
        Gets all campaigns or specific one if campaign_id is not None
        """
        return await super(Campaign, self).get(campaign_id)

    async def get_deleted(self):
        """
        Gets all deleted/archived campaigns
        """
        return await super(Campaign, self).get('deleted')

    async def get_streams(self, campaign_id):
        """
        Gets streams of campaign with campaign_id
        """
        return await super(Campaign, self).get(campaign_id, 'streams')

    async def clone(self, campaign_id):
        """
        Clones campaign by its campaign_id
        """
        return await super(Campaign, self).post(campaign_id)

    async def create(self, name, *, alias=None, type=None,
               state=None, cost_type=None, cookies_ttl=None, cost_value=None,
               cost_currency=None, cost_auto=False, group_id=None, token=None,
               traffic_source_id=None, bind_visitors=None, parameters=None,
               domain_id=None, postbacks=None):
        """
        Creates new advertising campaign
        """
        query_params = remove_key_values(locals())
        query_params['alias'] = await generate_random_string()
        return await super(Campaign, self).post(**query_params)

    async def disable(self, campaign_id):
        """
        Changes state of campaign to disabled
        """
        return await super(Campaign, self).post(campaign_id, 'disable')

    async def get_by_name(self, name):
        """
        Returns list of found campaigns by name
        """
        return await filter_resource_entities_by_key_value(
            (await self.get()).json(), 'name', name)

    async def enable(self, campaign_id):
        """
        Changes state of campaign to active
        """
        return await super(Campaign, self).post(campaign_id, 'enable')

    async def restore(self, campaign_id):
        """
        Restores campaign from archive
        """
        return await super(Campaign, self).post(campaign_id, 'restore')

    async def update_costs(self, campaign_id, *, start_date, end_date, timezone,
                     cost, currency, only_campaign_uniques=None, filters=None):
        """
        Updates campaign costs
        """
        query_params = remove_key_values(locals())
        return await super(Campaign, self).post(
            campaign_id, 'update_costs', **query_params)

    async def update(self, campaign_id, *, name=None, alias=None, type=None,
               state=None, cost_type=None, cookies_ttl=None, cost_value=None,
               cost_currency=None, cost_auto=False, group_id=None, token=None,
               traffic_source_id=None, bind_visitors=None, parameters=None,
               domain_id=None, postbacks=None):
        """
        Updates campaign data by campaign_id
        """
        return await super(Campaign, self).put(
            campaign_id, *remove_key_values(locals()))

