# coding=utf-8

from tvmaze.client import Client
from tvmaze.models import Show as ShowModel
from tvmaze.models import Episode as EpisodeModel
from tvmaze.models import Season as SeasonModel
from tvmaze.models import Cast as CastModel
from tvmaze.models import Crew as CrewModel
from tvmaze.models import Aka as AkaModel


class Show(Client):

    def __init__(self, **kwargs):
        super(Show, self).__init__(**kwargs)
        self.url = "shows"

    def list(self, page=0):
        result = self._get("/%s" % self.url, params={"page": page})
        return ShowModel.parse_list(result)

    def get(self, show_id):
        result = self._get("/%s/%s" % (self.url, show_id))
        return ShowModel.parse(result)

    def episodes(self, show_id):
        result = self._get("/%s/%s/episodes" % (self.url, show_id))
        return EpisodeModel.parse_list(result)

    def episode_by_number(self, show_id, season, number):
        result = self._get(
            "/%s/%s/episodebynumber" % (self.url, show_id), params={"season": season, "number": number}
        )
        return EpisodeModel.parse(result)

    def episodes_by_date(self, show_id, date):
        result = self._get("/%s/%s/episodesbydate" % (self.url, show_id), params={"date": date})
        return EpisodeModel.parse_list(result)

    def seasons(self, show_id):
        result = self._get("/%s/%s/seasons" % (self.url, show_id))
        return SeasonModel.parse_list(result)

    def cast(self, show_id):
        result = self._get("/%s/%s/cast" % (self.url, show_id))
        return CastModel.parse_list(result)

    def crew(self, show_id):
        result = self._get("/%s/%s/crew" % (self.url, show_id))
        return CrewModel.parse_list(result)

    def akas(self, show_id):
        result = self._get("/%s/%s/akas" % (self.url, show_id))
        return AkaModel.parse_list(result)
