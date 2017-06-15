from tvmaze.character import Character
from tvmaze.episode import Episode
from tvmaze.network import Network
from tvmaze.people import People
from tvmaze.schedule import Schedule
from tvmaze.search import Search
from tvmaze.show import Show
from tvmaze.webchannel import WebChannel


class Api(object):
    BASE_URL = "http://api.tvmaze.com"

    def __init__(self, **kwargs):
        """
        TvMaze Api
        :param kwargs:
        """
        self.base_url = self.BASE_URL

    @property
    def show(self):
        return Show(api=self)

    @property
    def people(self):
        return People(api=self)

    @property
    def schedule(self):
        return Schedule(api=self)

    @property
    def episode(self):
        return Episode(api=self)

    @property
    def search(self):
        return Search(api=self)

    @property
    def network(self):
        return Network(api=self)

    @property
    def character(self):
        return Character(api=self)

    @property
    def web_channel(self):
        return WebChannel(api=self)
