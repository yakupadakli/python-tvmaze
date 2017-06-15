# coding=utf-8

from tvmaze.client import Client
from tvmaze.models import Character as CharacterModel


class Character(Client):

    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)
        self.url = "characters"

    def get(self, character_id):
        result = self._get("/%s/%s" % (self.url, character_id))
        return CharacterModel.parse(result)
