

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
        state = ['%s=%s' % (self._repr_values[k], repr(v)) for (k, v) in items]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(state))


class Show(Model):

    def __init__(self, **kwargs):
        super(Show, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}


class Episode(Model):

    def __init__(self, **kwargs):
        super(Episode, self).__init__(**kwargs)
        self._repr_values = {"name": "Name", "season": "Season", "number": "Episode"}


class Season(Model):

    def __init__(self, **kwargs):
        super(Season, self).__init__(**kwargs)
        self._repr_values = {"number": "Season"}


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


class Character(Model):

    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)
        self._repr_values = {"name": "Name"}


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
