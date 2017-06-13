# coding=utf-8

from tvmaze.client import Client
from tvmaze.models import Episode as EpisodeModel


class Schedule(Client):

    def __init__(self, **kwargs):
        super(Schedule, self).__init__(**kwargs)
        self.url = "schedule"

    def today(self):
        result = self._get("/%s" % self.url)
        return EpisodeModel.parse_list(result)

    def filter(self, country_code=None, date=None):
        result = self._get("/%s" % self.url, params={"country": country_code, "date": date})
        return EpisodeModel.parse_list(result)

    def full(self):
        result = self._get("/%s/full" % self.url)
        return EpisodeModel.parse_list(result)
