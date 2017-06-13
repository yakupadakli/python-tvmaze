from tvmaze.people import People
from tvmaze.schedule import Schedule
from tvmaze.show import Show


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
