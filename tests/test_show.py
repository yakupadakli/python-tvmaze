# -*- coding: utf-8 -*-

import unittest

from tvmaze.api import Api
from tvmaze.models import Show, Episode, Season, Cast, Crew, Aka


class ShowTests(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_show_list(self):
        show_list = self.api.show.list()
        self.assertIsInstance(show_list, list)
        self.assertIsInstance(show_list[0], Show)

    def test_show_get(self):
        show = self.api.show.get(1)
        self.assertIsInstance(show, Show)

    def test_show_episodes(self):
        episode_list = self.api.show.episodes(1)
        self.assertIsInstance(episode_list, list)
        self.assertIsInstance(episode_list[0], Episode)

    def test_show_episode_by_number(self):
        episode = self.api.show.episode_by_number(1, season=1, number=1)
        self.assertIsInstance(episode, Episode)

    def test_show_episodes_by_date(self):
        episode_list = self.api.show.episodes_by_date(1, "2013-07-01")
        self.assertIsInstance(episode_list, list)
        self.assertIsInstance(episode_list[0], Episode)

    def test_show_seasons(self):
        season_list = self.api.show.seasons(1)
        self.assertIsInstance(season_list, list)
        self.assertIsInstance(season_list[0], Season)

    def test_show_cast(self):
        cast_list = self.api.show.cast(1)
        self.assertIsInstance(cast_list, list)
        self.assertIsInstance(cast_list[0], Cast)

    def test_show_crew(self):
        crew_list = self.api.show.crew(1)
        self.assertIsInstance(crew_list, list)
        self.assertIsInstance(crew_list[0], Crew)

    def test_show_akas(self):
        akas_list = self.api.show.akas(1)
        self.assertIsInstance(akas_list, list)
        self.assertIsInstance(akas_list[0], Aka)
