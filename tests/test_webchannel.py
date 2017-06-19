# -*- coding: utf-8 -*-

import unittest

from tvmaze.api import Api
from tvmaze.models import WebChannel


class WebChannelTests(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_web_channel_get(self):
        web_channel = self.api.web_channel.get(1)
        self.assertIsInstance(web_channel, WebChannel)
