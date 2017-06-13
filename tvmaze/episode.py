# coding=utf-8

from tvmaze.client import Client
from tvmaze.models import Episode as EpisodeModel


class Episode(Client):

    def __init__(self, **kwargs):
        super(Episode, self).__init__(**kwargs)
        self.url = "episodes"

    def get(self, episode_id):
        result = self._get("/%s/%s" % (self.url, episode_id))
        return EpisodeModel.parse(result)
