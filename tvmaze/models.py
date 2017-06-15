

class ResultSet(list):
    """A list like object that holds results from a  API query."""


class Model(object):

    def __init__(self, **kwargs):
        self._repr_values = {"id": "ID"}

    @classmethod
    def parse(cls, data):
        data = data or {}
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
        return '<%s: %s: >' % (self.__class__.__name__, ', '.join(state))


class Show(Model):

    def __init__(self, **kwargs):
        super(Show, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data):
        show = super(Show, cls).parse(data)
        if hasattr(show, "image"):
            show.image = Image.parse(show.image)
        if hasattr(show, "network"):
            show.network = Network.parse(show.network)
        if hasattr(show, "externals"):
            show.externals = External.parse(show.externals)
        if hasattr(show, "rating"):
            show.rating = Rating.parse(show.rating)
        if hasattr(show, "schedule"):
            show.schedule = Schedule.parse(show.schedule)
        if hasattr(show, "webChannel"):
            show.webChannel = WebChannel.parse(show.webChannel)
        return show


class Episode(Model):

    def __init__(self, **kwargs):
        super(Episode, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "season": "Season", "number": "Episode"}

    @classmethod
    def parse(cls, data):
        episode = super(Episode, cls).parse(data)
        if hasattr(episode, "show"):
            episode.show = Show.parse(episode.show)
        return episode


class Season(Model):

    def __init__(self, **kwargs):
        super(Season, self).__init__(**kwargs)
        self._repr_values = {"number": "Season"}

    @classmethod
    def parse(cls, data):
        season = super(Season, cls).parse(data)
        if hasattr(season, "network"):
            season.network = Network.parse(season.network)
        if hasattr(season, "image"):
            season.image = Image.parse(season.image)
        return season


class Cast(Model):

    @classmethod
    def parse(cls, data):
        cast = super(Cast, cls).parse(data)
        if hasattr(cast, "person"):
            cast.person = Person.parse(cast.person)
        if hasattr(cast, "character"):
            cast.character = Character.parse(cast.character)
        return cast


class Person(Model):

    def __init__(self, **kwargs):
        super(Person, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data):
        person = super(Person, cls).parse(data)
        if hasattr(person, "image"):
            person.image = Image.parse(person.image)
        return person


class Character(Model):

    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data):
        character = super(Character, cls).parse(data)
        if hasattr(character, "image"):
            character.image = Image.parse(character.image)
        return character


class Crew(Model):

    def __init__(self, **kwargs):
        super(Crew, self).__init__(**kwargs)
        self._repr_values = {"type": "Type"}

    @classmethod
    def parse(cls, data):
        crew = super(Crew, cls).parse(data)
        if hasattr(crew, "person"):
            crew.person = Person.parse(crew.person)
        return crew


class Aka(Model):

    def __init__(self, **kwargs):
        super(Aka, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data):
        aka = super(Aka, cls).parse(data)
        if hasattr(aka, "country"):
            aka.country = Country.parse(aka.country)
        return aka


class Country(Model):

    def __init__(self, **kwargs):
        super(Country, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "code": "Code"}


class People(Model):

    def __init__(self, **kwargs):
        super(People, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data):
        people = super(People, cls).parse(data)
        if hasattr(people, "image"):
            people.image = Image.parse(people.image)
        return people


class Image(Model):
    pass


class CastCredit(Model):

    @classmethod
    def parse(cls, data):
        cast_credit = super(CastCredit, cls).parse(data)
        if hasattr(cast_credit, "_embedded"):
            character = cast_credit._embedded.get("character")
            cast_credit.character = Character.parse(character)

            show = cast_credit._embedded.get("show")
            cast_credit.show = Show.parse(show)
        return cast_credit


class CrewCredit(Model):

    def __init__(self, **kwargs):
        super(CrewCredit, self).__init__(**kwargs)
        self._repr_values = {"type": "Type"}

    @classmethod
    def parse(cls, data):
        crew_credit = super(CrewCredit, cls).parse(data)
        if hasattr(crew_credit, "_embedded"):
            show = crew_credit._embedded.get("show")
            crew_credit.show = Show.parse(show)
        return crew_credit


class Network(Model):

    def __init__(self, **kwargs):
        super(Network, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}

    @classmethod
    def parse(cls, data):
        network = super(Network, cls).parse(data)
        if hasattr(network, "country"):
            network.country = Country.parse(network.country)
        return network


class External(Model):

    def __init__(self, **kwargs):
        super(External, self).__init__(**kwargs)
        self._repr_values = {"imdb": "IMDB"}


class Rating(Model):

    def __init__(self, **kwargs):
        super(Rating, self).__init__(**kwargs)
        self._repr_values = {"average": "Average"}


class Schedule(Model):

    def __init__(self, **kwargs):
        super(Schedule, self).__init__(**kwargs)
        self._repr_values = {"time": "Time", "days": "Days"}


class WebChannel(Model):

    def __init__(self, **kwargs):
        super(WebChannel, self).__init__(**kwargs)
        self._repr_values = {"time": "Time", "days": "Days"}

    @classmethod
    def parse(cls, data):
        web_channel = super(WebChannel, cls).parse(data)
        if hasattr(web_channel, "country"):
            web_channel.country = Country.parse(web_channel.country)
        return web_channel
