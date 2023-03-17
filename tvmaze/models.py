from tvmaze import expections


class ResultSet(list):
    """A list like object that holds results from a  API query."""


class Model(object):
    not_found_error_class = expections.NotFound

    def __init__(self, **kwargs):
        self._repr_values = {"id": "ID"}

    @classmethod
    def parse(cls, data, sub_item=False):
        data = data or {}
        if not data and not sub_item:
            raise cls.not_found_error_class()
        instance = cls() if data else None
        for key, value in data.items():
            if type(value) == str:
                value = value.strip()
            setattr(instance, key, value)
        return instance

    @classmethod
    def parse_list(cls, data):
        results = ResultSet()
        data = data or []
        for obj in data:
            if obj:
                results.append(cls.parse(obj))
        return results

    def __repr__(self):
        items = filter(lambda x: x[0] in self._repr_values.keys(), vars(self).items())
        state = ['%s: %s' % (self._repr_values[k], repr(v)) for (k, v) in items]
        return '<%s: %s >' % (self.__class__.__name__, ', '.join(state))


class Show(Model):
    not_found_error_class = expections.ShowNotFound

    def __init__(self, **kwargs):
        super(Show, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data, sub_item=False):
        show = super(Show, cls).parse(data, sub_item=sub_item)
        if hasattr(show, "image"):
            show.image = Image.parse(show.image, sub_item=True)
        if hasattr(show, "network"):
            show.network = Network.parse(show.network, sub_item=True)
        if hasattr(show, "externals"):
            show.externals = External.parse(show.externals, sub_item=True)
        if hasattr(show, "rating"):
            show.rating = Rating.parse(show.rating, sub_item=True)
        if hasattr(show, "schedule"):
            show.schedule = Schedule.parse(show.schedule, sub_item=True)
        if hasattr(show, "webChannel"):
            show.webChannel = WebChannel.parse(show.webChannel, sub_item=True)
        return show


class Episode(Model):
    not_found_error_class = expections.EpisodeNotFound

    def __init__(self, **kwargs):
        super(Episode, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "season": "Season", "number": "Episode"}

    @classmethod
    def parse(cls, data, sub_item=False):
        episode = super(Episode, cls).parse(data, sub_item=sub_item)
        if hasattr(episode, "show"):
            episode.show = Show.parse(episode.show, sub_item=True)
        return episode


class Season(Model):
    not_found_error_class = expections.SeasonNotFound

    def __init__(self, **kwargs):
        super(Season, self).__init__(**kwargs)
        self._repr_values = {"number": "Season"}

    @classmethod
    def parse(cls, data, sub_item=False):
        season = super(Season, cls).parse(data, sub_item=sub_item)
        if hasattr(season, "network"):
            season.network = Network.parse(season.network, sub_item=True)
        if hasattr(season, "image"):
            season.image = Image.parse(season.image, sub_item=True)
        return season


class Cast(Model):
    not_found_error_class = expections.ShowNotFound

    @classmethod
    def parse(cls, data, sub_item=False):
        cast = super(Cast, cls).parse(data, sub_item=sub_item)
        if hasattr(cast, "person"):
            cast.person = Person.parse(cast.person, sub_item=True)
        if hasattr(cast, "character"):
            cast.character = Character.parse(cast.character, sub_item=True)
        return cast


class Person(Model):
    not_found_error_class = expections.PersonNotFound

    def __init__(self, **kwargs):
        super(Person, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data, sub_item=False):
        person = super(Person, cls).parse(data, sub_item=sub_item)
        if hasattr(person, "image"):
            person.image = Image.parse(person.image, sub_item=True)
        return person


class Character(Model):
    not_found_error_class = expections.CharacterNotFound

    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data, sub_item=False):
        character = super(Character, cls).parse(data, sub_item=sub_item)
        if hasattr(character, "image"):
            character.image = Image.parse(character.image, sub_item=True)
        return character


class Crew(Model):
    not_found_error_class = expections.CrewNotFound

    def __init__(self, **kwargs):
        super(Crew, self).__init__(**kwargs)
        self._repr_values = {"type": "Type"}

    @classmethod
    def parse(cls, data, sub_item=False):
        crew = super(Crew, cls).parse(data, sub_item=sub_item)
        if hasattr(crew, "person"):
            crew.person = Person.parse(crew.person, sub_item=True)
        return crew


class Aka(Model):
    not_found_error_class = expections.AkaNotFound

    def __init__(self, **kwargs):
        super(Aka, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data, sub_item=False):
        aka = super(Aka, cls).parse(data, sub_item=sub_item)
        if hasattr(aka, "country"):
            aka.country = Country.parse(aka.country, sub_item=True)
        return aka


class Country(Model):
    not_found_error_class = expections.CountryNotFound

    def __init__(self, **kwargs):
        super(Country, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "code": "Code"}


class People(Model):
    not_found_error_class = expections.PeopleNotFound

    def __init__(self, **kwargs):
        super(People, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data, sub_item=False):
        people = super(People, cls).parse(data, sub_item=sub_item)
        if hasattr(people, "image"):
            people.image = Image.parse(people.image, sub_item=True)
        return people


class Image(Model):
    not_found_error_class = expections.ImageNotFound

    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)
        self._repr_values = {"id": "ID", "type": "Type"}

    @classmethod
    def parse(cls, data, sub_item=False):
        image = super(Image, cls).parse(data, sub_item=sub_item)
        if hasattr(image, "resolutions"):
            image.resolutions = Resolution.parse(image.resolutions, sub_item=True)
        return image


class CastCredit(Model):
    not_found_error_class = expections.CastCreditNotFound

    @classmethod
    def parse(cls, data, sub_item=False):
        cast_credit = super(CastCredit, cls).parse(data, sub_item=sub_item)
        if hasattr(cast_credit, "_embedded"):
            character = cast_credit._embedded.get("character")
            cast_credit.character = Character.parse(character, sub_item=True)

            show = cast_credit._embedded.get("show")
            cast_credit.show = Show.parse(show, sub_item=True)
        return cast_credit


class CrewCredit(Model):
    not_found_error_class = expections.CrewCreditNotFound

    def __init__(self, **kwargs):
        super(CrewCredit, self).__init__(**kwargs)
        self._repr_values = {"type": "Type"}

    @classmethod
    def parse(cls, data, sub_item=False):
        crew_credit = super(CrewCredit, cls).parse(data, sub_item=sub_item)
        if hasattr(crew_credit, "_embedded"):
            show = crew_credit._embedded.get("show")
            crew_credit.show = Show.parse(show, sub_item=True)
        return crew_credit


class Network(Model):
    not_found_error_class = expections.NetworkNotFound

    def __init__(self, **kwargs):
        super(Network, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data, sub_item=False):
        network = super(Network, cls).parse(data, sub_item=sub_item)
        if hasattr(network, "country"):
            network.country = Country.parse(network.country, sub_item=True)
        return network


class External(Model):
    not_found_error_class = expections.ExternalNotFound

    def __init__(self, **kwargs):
        super(External, self).__init__(**kwargs)
        self._repr_values = {"imdb": "IMDB", "tvrage": "TVRage", "thetvdb": "TheTVDB"}


class Rating(Model):
    not_found_error_class = expections.RatingNotFound

    def __init__(self, **kwargs):
        super(Rating, self).__init__(**kwargs)
        self._repr_values = {"average": "Average"}


class Schedule(Model):
    not_found_error_class = expections.ScheduleNotFound

    def __init__(self, **kwargs):
        super(Schedule, self).__init__(**kwargs)
        self._repr_values = {"time": "Time", "days": "Days"}


class WebChannel(Model):
    not_found_error_class = expections.WebChannelNotFound

    def __init__(self, **kwargs):
        super(WebChannel, self).__init__(**kwargs)
        self._repr_values = {"time": "Time", "days": "Days"}

    @classmethod
    def parse(cls, data, sub_item=False):
        web_channel = super(WebChannel, cls).parse(data, sub_item=sub_item)
        if hasattr(web_channel, "country"):
            web_channel.country = Country.parse(web_channel.country, sub_item=True)
        return web_channel


class Resolution(Model):
    not_found_error_class = expections.ResolutionNotFound

    @classmethod
    def parse(cls, data, sub_item=False):
        resolution = super(Resolution, cls).parse(data, sub_item=sub_item)
        if hasattr(resolution, "original"):
            resolution.original = Model.parse(resolution.original, sub_item=True)
        if hasattr(resolution, "medium"):
            resolution.medium = Model.parse(resolution.medium, sub_item=True)
        return resolution
