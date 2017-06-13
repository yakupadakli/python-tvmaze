# coding=utf-8

from tvmaze.client import Client
from tvmaze.models import Show as ShowModel
from tvmaze.models import People as PeopleModel


class Search(Client):

    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)
        self.search_url = "search"
        self.single_search_url = "singlesearch"
        self.lookup_url = "lookup"
        self.lookup_fields = ["tvrage", "thetvdb", "imdb"]

    def shows(self, query):
        result = self._get("/%s/shows" % self.search_url, params={"q": query})
        return ShowModel.parse_list(map(lambda x: x.get("show"), result))

    def single_show(self, query):
        result = self._get("/%s/shows" % self.single_search_url, params={"q": query})
        return ShowModel.parse(result)

    def lookup_show(self, lookup_id, lookup_option):
        if lookup_option not in self.lookup_fields:
            raise Exception("Invalid lookup option")
        result = self._get("/%s/shows" % self.lookup_url, params={lookup_option: lookup_id})
        return ShowModel.parse(result)

    def people(self, query):
        result = self._get("/%s/people" % self.search_url, params={"q": query})
        return PeopleModel.parse_list(map(lambda x: x.get("person"), result))
