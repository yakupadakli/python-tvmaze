import six


class TvMazeException(Exception):
    message = six.text_type("Unknown error")

    def __init__(self, message=None, status=None, **kwargs):
        self.message = six.text_type(message) if message else self.message
        self.status = status
        super(TvMazeException, self).__init__(message, status, **kwargs)

    def __str__(self):
        return self.message


class ConnectionError(TvMazeException):
    pass


class NotFound(TvMazeException):
    message = six.text_type("Not Found")


class ShowNotFound(NotFound):
    message = six.text_type("Show Not Found")


class EpisodeNotFound(NotFound):
    message = six.text_type("Episode Not Found")


class SeasonNotFound(NotFound):
    message = six.text_type("Season Not Found")


class CastNotFound(NotFound):
    message = six.text_type("Cast Not Found")


class PersonNotFound(NotFound):
    message = six.text_type("Person Not Found")


class CharacterNotFound(NotFound):
    message = six.text_type("Character Not Found")


class CrewNotFound(NotFound):
    message = six.text_type("Crew Not Found")


class AkaNotFound(NotFound):
    message = six.text_type("Aka Not Found")


class CountryNotFound(NotFound):
    message = six.text_type("Country Not Found")


class PeopleNotFound(NotFound):
    message = six.text_type("People Not Found")


class ImageNotFound(NotFound):
    message = six.text_type("Image Not Found")


class CastCreditNotFound(NotFound):
    message = six.text_type("Cast Credit Not Found")


class CrewCreditNotFound(NotFound):
    message = six.text_type("Crew Credit Not Found")


class NetworkNotFound(NotFound):
    message = six.text_type("Network Not Found")


class ExternalNotFound(NotFound):
    message = six.text_type("External Not Found")


class RatingNotFound(NotFound):
    message = six.text_type("Rating Not Found")


class ScheduleNotFound(NotFound):
    message = six.text_type("Schedule Not Found")


class WebChannelNotFound(NotFound):
    message = six.text_type("Web Channel Not Found")


class ResolutionNotFound(NotFound):
    message = six.text_type("Resolution Not Found")
