# coding=utf-8

from tvmaze.client import Client
from tvmaze.models import WebChannel as WebChannelModel


class WebChannel(Client):

    def __init__(self, **kwargs):
        super(WebChannel, self).__init__(**kwargs)
        self.url = "webchannels"

    def get(self, web_channel_id):
        result = self._get("/%s/%s" % (self.url, web_channel_id))
        return WebChannelModel.parse(result)
