from aiokeitaro.api import API


class Report(API):

    def __init__(self, client, endpoint='report'):
        super(Report, self).__init__(client, endpoint)

    async def get_labels(self, campaign_id, label_name, ref_name):
        """
        Gets reports labels
        """
        return await super(Report, self).get(
            'labels', campaign_id=campaign_id,
            label_name=label_name, ref_name=ref_name)

    async def build(
            self, interval, timezone,
            metrics=['clicks', 'campaign_unique_clicks', 'conversions', 'roi'],
            grouping=['campaign'], sort={'name': 'clicks', 'order': 'DESC'}):
        """
        Builds custom keitaro report
        """
        return await super(Report, self).post(
            'build', range={'interval': interval, 'timezone': timezone},
            metrics=metrics, grouping=grouping, sort=[sort])

    async def update_labels(self, campaign_id, ref_name, items):
        """
        Updates report labels
        """
        return await super(Report, self).post(
            'labels', campaign_id=campaign_id,
            ref_name=ref_name, items={'value': items})
