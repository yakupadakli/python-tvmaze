# -*- coding: utf-8 -*-

import unittest

from tvmaze.api import Api
from tvmaze.models import Episode


class EpisodeTests(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_episode_get(self):
        episode = self.api.episode.get(1)
        self.assertIsInstance(episode, Episode)
