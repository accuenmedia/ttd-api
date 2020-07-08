import config

import unittest
import json
import time

from ttdclient.service.connection import Connection

from ttdclient.models.ad_group import AdGroup
from ttdclient.models.advertiser import Advertiser
from ttdclient.models.campaign import Campaign
from ttdclient.models.contract import Contract
from ttdclient.models.site_list import SiteList
from tests.base import Base


class AdGroupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = Connection(
            username=config.username,
            password=config.password,
            url=config.url
        )

    def testGetAdGroup(self):
        loader = AdGroup(AdGroupTest.conn)
        ad_group = loader.find('8531y0h')
        ad_group = json.loads(ad_group).get('data')
        self.assertEqual(ad_group.get('AdGroupId'), '8531y0h')

    def testGetByCampaign(self):
        loader = AdGroup(AdGroupTest.conn)
        ad_groups = loader.get_by_campaign(config.campaign_id, active_only=False)
        import json
        ads = json.loads(ad_groups) 
        self.assertEqual(len(ads.get('data')), 342)

        ad_groups = loader.get_by_campaign(config.campaign_id, active_only=True)
        ad_groups = json.loads(ad_groups).get("data").get("Result")
        self.assertEqual(len(ad_groups), 195)
