# coding=utf-8

from tvmaze.client import Client
from tvmaze.models import Network as NetworkModel


class Network(Client):

    def __init__(self, **kwargs):
        super(Network, self).__init__(**kwargs)
        self.url = "networks"

    def get(self, network_id):
        result = self._get("/%s/%s" % (self.url, network_id))
        return NetworkModel.parse(result)
