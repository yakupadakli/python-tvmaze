# python-tvmaze

A library that provides a Python interface to [the TvMaze API](http://www.tvmaze.com/api).

## Installation

The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    pip install python-tvmaze

You may also use Git to clone the repository from
Github and install it manually:

    git clone https://github.com/yakupadakli/python-tvmaze.git
    cd python-tvmaze
    python setup.py install

Python 3.8, 3.9 and 3.11 is supported for now.

## Usage

    from tvmaze.api import Api
    api = Api()

### Shows

##### Show list

A list of all shows, with all primary information included. 

    api.show.list()  # default page is 0
    api.show.list(page=1)

##### Show get

Retrieve all primary information for a given show.

    api.show.get(1)

##### Show episode list

A complete list of episodes for the given show.

    api.show.episodes(1)

##### Show episode by number

Retrieve one specific episode from this show given its season number and episode number.

    api.show.episode_by_number(1)

##### Show episode by number

Retrieve one specific episode from this show given its season number and episode number.

    api.show.episode_by_number(1, season=1, number=1)

##### Show episode by date

Retrieve all episodes from this show that have aired on a specific date.

    api.show.episodes_by_date(1, "2013-07-01")

##### Show seasons

A complete list of seasons for the given show.

    api.show.seasons(1)

##### Show cast

A list of main cast for a show.

    api.show.cast(1)

##### Show crew

A list of main crew for a show.

    api.show.crew(1)

##### Show AKA's

A list of AKA's (aliases) for a show. 
An AKA with its country set to null indicates an AKA in the show's original country.

    api.show.akas(1)


---


### People

##### Person get

Retrieve all primary information for a given person.

    api.people.get(1)

##### Person cast credits

Retrieve all (show-level) cast credits for a person.

    api.people.cast_credits(1)

##### Person crew credits

Retrieve all (show-level) crew credits for a person.

    api.people.crew_credits(100)


---


### Schedule

##### Today schedule

The schedule is a complete list of episodes that air today.

    api.schedule.today()

##### Schedule by country and date

The schedule is a complete list of episodes that air in a given country on a given date.

    api.schedule.filter(country_code="US", date="2014-12-01")

##### Full schedule

The full schedule is a list of all future episodes known to TVmaze, regardless of their country.

    api.schedule.full()


---


### Search

##### Search show

Search through all the shows by the show's name.

    api.search.shows("girls")

##### Search single show

Search through all the shows by the show's name and the 
single search endpoint which either returns exactly one result, or no result at all.

    api.search.single_show("girls")

##### Lookup show

If you already know a show's tvrage, thetvdb or IMDB ID, 
you can use this endpoint to find this exact show on TVmaze

    api.search.lookup_show("tvrage", "24493")
    api.search.lookup_show("thetvdb", "81189")
    api.search.lookup_show("imdb", "tt0944947")

##### Search people

Search through all the people by the name.

    api.search.people("lauren")


---


### Character

##### Character get

Retrieve all primary information for a given character.

    api.character.get(1)


---


### Episode

##### Episode get

Retrieve all primary information for a given episode.

    api.episode.get(1)


---


### Network

##### Network get

Retrieve all primary information for a given network.

    api.network.get(1)


---


### WebChannel

##### Web Channel get

Retrieve all primary information for a given web channel.

    api.web_channel.get(1)
