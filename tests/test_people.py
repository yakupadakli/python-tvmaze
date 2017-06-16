# -*- coding: utf-8 -*-

import unittest

from tvmaze.api import Api
from tvmaze.models import People, CastCredit, CrewCredit


class PeopleTests(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_people_get(self):
        people = self.api.people.get(1)
        self.assertIsInstance(people, People)

    def test_people_cast_credits(self):
        cast_credit_list = self.api.people.cast_credits(1)
        self.assertIsInstance(cast_credit_list, list)
        self.assertIsInstance(cast_credit_list[0], CastCredit)

    def test_people_crew_credits(self):
        crew_credit_list = self.api.people.crew_credits(100)
        self.assertIsInstance(crew_credit_list, list)
        self.assertIsInstance(crew_credit_list[0], CrewCredit)
