# -*- coding: utf-8 -*-

import unittest

from tvmaze.api import Api
from tvmaze.models import Character


class CharacterTests(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_character_get(self):
        network = self.api.character.get(1)
        self.assertIsInstance(network, Character)
