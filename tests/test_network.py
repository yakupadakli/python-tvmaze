# -*- coding: utf-8 -*-

import unittest

from tvmaze.api import Api
from tvmaze.models import Network


class NetworkTests(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_network_get(self):
        network = self.api.network.get(1)
        self.assertIsInstance(network, Network)
