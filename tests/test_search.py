# -*- coding: utf-8 -*-

import unittest

from tvmaze.api import Api
from tvmaze.models import Show, People


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_search_shows(self):
        shows = self.api.search.shows("girls")
        self.assertIsInstance(shows, list)
        self.assertIsInstance(shows[0], Show)

    def test_search_single_show(self):
        show = self.api.search.single_show("girls")
        self.assertIsInstance(show, Show)

    def test_search_lookup_show(self):
        show1 = self.api.search.lookup_show("tvrage", "24493")
        show2 = self.api.search.lookup_show("thetvdb", "81189")
        show3 = self.api.search.lookup_show("imdb", "tt0944947")
        self.assertIsInstance(show1, Show)
        self.assertIsInstance(show2, Show)
        self.assertIsInstance(show3, Show)

    def test_search_people(self):
        people = self.api.search.people("lauren")
        self.assertIsInstance(people, list)
        self.assertIsInstance(people[0], People)
