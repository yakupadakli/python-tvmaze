import requests


class Client(object):
    """
    TvMaze Client

    HTTP connections to and communication with the TvMaze API.
    """

    def __init__(self, api, **kwargs):
        self.api = api

    def _request(self, url, method, params=None, data=None, headers=None, **kwargs):
        url = "%s%s" % (self.api.base_url, url)

        try:
            response = requests.request(method, url, params=params, data=data, headers=headers, **kwargs)
        except Exception, e:
            raise Exception("Connection error: %s" % e)

        try:
            """
            {u'status': 404, u'message': u'Page not found.', u'code': 0, u'name': u'Not Found', 
            u'previous': {u'message': u'Unable to resolve the request "shows/1/episodes/".', 
            u'code': 0, u'name': u'Invalid Route'}}
            """
            if not self._is_2xx(response.status_code):
                message = response.json().get("message")
                raise Exception(message)
            result = response.json()
        except ValueError:
            result = None
        return result

    def _get(self, url, params=None, **kwargs):
        return self._request(url, "get", params=params, **kwargs)

    def _post(self, url, data=None, **kwargs):
        return self._request(url, "post", data=data, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request(url, "delete", **kwargs)

    def _put(self, url, data=None, **kwargs):
        return self._request(url, "put", data=data, **kwargs)

    @staticmethod
    def _is_1xx(status_code):
        return 100 <= status_code <= 199

    @staticmethod
    def _is_2xx(status_code):
        return 200 <= status_code <= 299

    @staticmethod
    def _is_3xx(status_code):
        return 300 <= status_code <= 399

    @staticmethod
    def _is_4xx(status_code):
        return 400 <= status_code <= 499

    @staticmethod
    def _is_5xx(status_code):
        return 500 <= status_code <= 599
