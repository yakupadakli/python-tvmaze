# coding=utf-8

from tvmaze.client import Client
from tvmaze.models import People as PeopleModel
from tvmaze.models import CastCredit as CastCreditModel
from tvmaze.models import CrewCredit as CrewCreditModel


class People(Client):

    def __init__(self, **kwargs):
        super(People, self).__init__(**kwargs)
        self.url = "people"

    def get(self, people_id):
        result = self._get("/%s/%s" % (self.url, people_id))
        return PeopleModel.parse(result)

    def cast_credits(self, people_id):
        params = {"embed[]": ["show", "character"]}
        result = self._get("/%s/%s/castcredits" % (self.url, people_id), params=params)
        return CastCreditModel.parse_list(result)

    def crew_credits(self, people_id):
        result = self._get("/%s/%s/crewcredits" % (self.url, people_id), params={"embed": "show"})
        return CrewCreditModel.parse_list(result)
