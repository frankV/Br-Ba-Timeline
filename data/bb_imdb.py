# -*- coding: latin-1 -*-
from imdb import IMDb, helpers
from pprint import pprint as pp
import os, argparse, re
from datetime import date, timedelta
from bs4 import BeautifulSoup as bs4


class MyEpisode(object):
    """
    [u'music department', 'plot outline', 'camera and electrical department', u'distributors', 'rating', 'runtimes', 'costume designer', u'thanks', 'make up', 'year', 'production design', 'miscellaneous crew', 'color info', 'number of episodes', u'special effects department', 'visual effects', 'votes', 'producer', 'title', 'assistant director', 'writer', 'casting director', 'episode of', 'production manager', 'set decoration', 'editor', 'certificates', u'costume department', 'country codes', 'language codes', 'cover url', u'casting department', 'special effects companies', 'season', 'sound mix', 'genres', u'production companies', 'stunt performer', 'miscellaneous companies', 'cinematographer', 'art direction', 'original air date', 'sound crew', 'director', 'kind', 'episode', u'art department', 'languages', u'transportation department', 'countries', 'cast', 'original music', u'editorial department']
    """

    def __init__(self, episode, id, episode_dates):
        self.id = int(id)
        self.season = episode.data['season'] if episode.data.has_key('season') else ''
        self.number = episode.data['episode'] if episode.data.has_key('episode') else ''
        self.title = episode.data['title'] if episode.data.has_key('title') else ''
        self.released = episode.data['original air date'] if episode.data.has_key('original air date') else ''
        self.runtime = episode.data['runtimes'] if episode.data.has_key('runtimes') else ''
        self.rating = episode.data['rating'] if episode.data.has_key('rating') else ''
        self.storyline = episode.data['plot outline'] if episode.data.has_key('plot outline') else ''
        self.photos = episode.data['cover url'] if episode.data.has_key('cover url') else ''
        self.keywords = episode.data['genres'] if episode.data.has_key('genres') else ''
        self.director = episode.data['director'] if episode.data.has_key('director') else ''
        self.writer = episode.data['writer'] if episode.data.has_key('writer') else ''

        self.quote = ''
        self.summary = ''
        self.time_since_pilot = ''
        self.calendar_start = ''
        self.calendar_end = ''

    def set_time(self, episode_dates):
        self.time_since_pilot = episode_dates['time_since_pilot']
        self.calendar_start = episode_dates['calendar_start']
        self.calendar_end = episode_dates['calendar_end']

    def to_dict(self):
        return dict(
            season = self.season,
            number = self.number,
            title = self.title,
            released = self.released,
            time_since_pilot = self.time_since_pilot,
            rating = self.rating,
            summary = self.summary,
            storyline = self.storyline,
            photos = self.photos,
            keywords = self.keywords,
            quote = self.quote,
            director = self.director,
            writer = self.writer,
            calendar_start = self.calendar_start,
            calendar_end = self.calendar_end,
            id = self.id
        )

    def __repr__(self):
        return '<Episode %r>' % (self.id)


def parse_args():
    """ argparse options

    usage: scrape-eps.py [-h] filename

    scrapes eps(episodes) from html file.

    positional arguments:
      filename    file to use

    optional arguments:
      -h, --help  show this help message and exit

    """
    parser = argparse.ArgumentParser(description='scrapes eps from html file.', fromfile_prefix_chars="@" )
    parser.add_argument('filename', help='file to use', action='store')
    args = parser.parse_args()
    return args


def parse_html(filename):

    cwd = os.getcwd()
    f = open(os.path.join(cwd, filename), 'r')

    Walters_Birthday = date(1957, 9, 7)
    Walter_Turns_50 = Walters_Birthday.replace(year = Walters_Birthday.year + 50)
    First_Calendar_Day = Walter_Turns_50

    eps_start_date = First_Calendar_Day
    eps_end_date = None
    weekDelta = 0
    dayDelta = 0

    # parsing
    html = bs4(f)   # souping
    if html.find('p', attrs={'class' : 'eps'}):
        all_episodes = []
        sections = html.findAll('p', attrs={'class' : 'eps'})
        for section in sections:
            if '<strong>' in str(section):
                title = section.find('strong')
                title = ''.join(title.findAll(text=True))

                eps_title = re.search(r'\"(.+?)\"', title)

                eps_season = re.search(r'(Season [0-9]+)', title)
                eps_number = re.search(r'(Episode [0-9]+)', title)
                season_id = re.search(r'[0-9]+', eps_season.group(0))
                episode_id = re.search(r'[0-9]+', eps_number.group(0))
                eps_tdelta = re.search(r'\((.*?)\)', title)

                eps_tdeltaWeek = re.search(r'([0-9]+ week?)', eps_tdelta.group(0))
                if eps_tdeltaWeek:
                    eps_tdeltaWeek = re.search(r'[0-9]+', eps_tdeltaWeek.group(0))
                    weeks = int(eps_tdeltaWeek.group(0))
                    weekDelta = timedelta(weeks = weeks)

                eps_tdeltaDay = re.search(r'([0-9]+ day?)', eps_tdelta.group(0))
                if eps_tdeltaDay:
                    eps_tdeltaDay = re.search(r'[0-9]+', eps_tdeltaDay.group(0))
                    days = int(eps_tdeltaWeek.group(0))
                    dayDelta = timedelta(days = days)

                if eps_end_date != None:
                    eps_start_date = last_eps_end_date
                    # last_eps_end_date isn't initialized (defined at the end of this
                    # function at the end of the first loop.. not sure what it's supposed to be.

                # add week delta
                if weekDelta != 0:
                    eps_end_date = First_Calendar_Day + weekDelta
                    weekDelta = 0   # reset weekDelta

                # add day delta
                if dayDelta != 0:
                    # print "and " + dayDelta.group(0) + " days"
                    eps_end_date = First_Calendar_Day + dayDelta
                    dayDelta = 0    # reset datDelta

                # set holder for this eps end date
                last_eps_end_date = eps_end_date

                ep = {}
                ep['season'] = season_id.group(0)
                ep['title'] = eps_title.group(0).replace(',', '').replace('"', '')
                ep['episode'] = episode_id.group(0)
                ep['time_since_pilot'] = eps_tdelta.group(0)
                ep['calendar_start'] = eps_start_date
                ep['calendar_end'] = eps_end_date
                print ep
                print ''
                all_episodes.append(ep)

        return all_episodes


def get_ep_from_movie(imdb_handler, movie):
    """
    Original function that'll probably get removed or repurposed.
    Don't worry about this for now.

    ['_Container__role', '__class__', '__cmp__', '__contains__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__len__', '__module__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_additional_keys', '_clear', '_get_currentRole', '_get_roleID', '_getitem', '_init', '_re_fullsizeURL', '_reset', '_roleClass', '_roleIsPerson', '_set_currentRole', '_set_roleID', 'accessSystem', 'add_to_current_info', 'append_item', 'asXML', 'charactersRefs', 'clear', 'cmpFunct', 'copy', 'currentRole', 'current_info', 'data', 'default_info', 'get', 'getAsXML', 'getID', 'get_charactersRefs', 'get_current_info', 'get_namesRefs', 'get_titlesRefs', 'guessLanguage', 'has_current_info', 'has_key', 'infoset2keys', 'isSame', 'isSameMovie', 'isSameTitle', 'items', 'iteritems', 'iterkeys', 'itervalues', 'key2infoset', 'keys', 'keys_alias', 'keys_tomodify', 'keys_tomodify_list', 'modFunct', 'movieID', 'myID', 'myTitle', 'namesRefs', 'notes', 'pop', 'popitem', 'reset', 'roleID', 'set_current_info', 'set_data', 'set_item', 'set_mod_funct', 'set_title', 'setdefault', 'smartCanonicalTitle', 'summary', 'titlesRefs', 'update', 'update_charactersRefs', 'update_infoset_map', 'update_namesRefs', 'update_titlesRefs', 'values']

    {'episode': 16,
     'episode of': <Movie id:0903747[http] title:_"Breaking Bad (TV Series 2008–2013)" (????)_>,
     'kind': u'episode',
     'original air date': u'29 Sep. 2013',
     'plot': u'\nWalt ties up whatever loose ends are left as the end draws near.    ',
     'season': 5,
     'title': u'Felina',
     'year': u'2013'}
    """
    imdb_handler.update(movie, 'episodes')
    for i in helpers.sortedSeasons(movie):
        print '\nSEASON ' + str(i) + ':'
        for ep in helpers.sortedEpisodes(movie, i):
            print ep['title']
            # pp(ep.__dict__, indent=2)
            # pp (ep.data)
            # pp (ep.movieID)


def get_ep_id_list(imdb_handler, movie):
    """
    Returns a list of episode IDs for a given movie object.
    """
    imdb_handler.update(movie, 'episodes')
    eps = []
    for i in helpers.sortedSeasons(movie):
        for ep in helpers.sortedEpisodes(movie, i):
            eps.append(ep.movieID)
    return eps


def get_all_episodes(imdb_handler, movie, episode_dates):
    """
    Returns a list of MyEpisode objects.
    """
    eps = []
    ep_ids = get_ep_id_list(imdb_handler, movie)

    for id in ep_ids:
        episode = MyEpisode(imdb_handler.get_movie(id), id, episode_dates)
        eps.append(episode)

    for i in xrange(len(episode_dates)):
        eps[i].set_time(episode_dates[i])

    return eps


def get_episode_images(ep_id):
    """
    Start of a function that will grab all the images from a given episode ID. Definitely not
    done.
    """
    url = 'http://www.imdb.com/title/'+ ep_id + '/mediaindex?ref_=tt_pv_mi_sm'
    return url


def main():
    # args = parse_args()   # filename using this is accessed by args.filename

    i = IMDb()

    # Some testing stuff for individual episodes
    # bb_5_2 = i.get_movie('2301457')     # Breaking Bad S5-E2 ID
    # print bb_5_2.data.keys()
    # print bb_5_2.data['color info']
    # print bb_5_2['cover url']
    # epi = MyEpisode(bb_5_2, '2301457')
    # print epi.to_dict()

    filename = "data/seasons_time_guide.html"
    episode_dates = parse_html(filename)

    bb = i.get_movie('0903747')       # Breaking Bad Series ID
    all_episodes = get_all_episodes(i, bb, episode_dates)

    for ep in all_episodes:
        pp(ep.to_dict())

    return all_episodes


if __name__ == '__main__':
    main()
