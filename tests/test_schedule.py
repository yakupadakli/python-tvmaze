# -*- coding: utf-8 -*-

import unittest

from tvmaze.api import Api
from tvmaze.models import Episode


class ScheduleTests(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_schedule_today(self):
        episodes = self.api.schedule.today()
        self.assertIsInstance(episodes, list)
        self.assertIsInstance(episodes[0], Episode)

    def test_schedule_filter(self):
        episodes = self.api.schedule.filter(country_code="US", date="2014-12-01")
        self.assertIsInstance(episodes, list)
        self.assertIsInstance(episodes[0], Episode)

    def test_schedule_full(self):
        episodes = self.api.schedule.full()
        self.assertIsInstance(episodes, list)
        self.assertIsInstance(episodes[0], Episode)
