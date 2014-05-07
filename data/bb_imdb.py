# -*- coding: latin-1 -*-
from imdb import IMDb, helpers
from pprint import pprint as pp


class MyEpisode(object):

    """
    [u'music department', 'plot outline', 'camera and electrical department', u'distributors', 'rating', 'runtimes', 'costume designer', u'thanks', 'make up', 'year', 'production design', 'miscellaneous crew', 'color info', 'number of episodes', u'special effects department', 'visual effects', 'votes', 'producer', 'title', 'assistant director', 'writer', 'casting director', 'episode of', 'production manager', 'set decoration', 'editor', 'certificates', u'costume department', 'country codes', 'language codes', 'cover url', u'casting department', 'special effects companies', 'season', 'sound mix', 'genres', u'production companies', 'stunt performer', 'miscellaneous companies', 'cinematographer', 'art direction', 'original air date', 'sound crew', 'director', 'kind', 'episode', u'art department', 'languages', u'transportation department', 'countries', 'cast', 'original music', u'editorial department']
    """

    def __init__(self, episode, id):
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

        # these are set scrapes-eps/py
        # self.duration = ''
        # self.calendar_start = ''
        # self.calendar_end = ''


    def to_dict(self):
        return dict(
            season = self.season,
            number = self.number,
            title = self.title,
            released = self.released,
            duration = self.duration,
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


def get_all_episodes(imdb_handler, movie):
    """
    Returns a list of MyEpisode objects.
    """
    eps = []
    ep_ids = get_ep_id_list(imdb_handler, movie)
    for id in ep_ids:
        episode = MyEpisode(imdb_handler.get_movie(id), id)
        eps.append(episode)
    # print dir(eps[1])
    # print eps[1].data
    return eps


def get_episode_images(ep_id):
    """
    Start of a function that will grab all the images from a given episode ID. Definitely not
    done.
    """
    url = 'http://www.imdb.com/title/'+ ep_id + '/mediaindex?ref_=tt_pv_mi_sm'
    return url


def main():
    i = IMDb()

    # Some testing stuff for individual episodes
    # bb_5_2 = i.get_movie('2301457')     # Breaking Bad S5-E2 ID
    # print bb_5_2.data.keys()
    # print bb_5_2.data['color info']
    # print bb_5_2['cover url']
    # epi = MyEpisode(bb_5_2, '2301457')
    # print epi.to_dict()

    bb = i.get_movie('0903747')       # Breaking Bad Series ID
    all_episodes = get_all_episodes(i, bb)
    for ep in all_episodes:
        pp(ep.to_dict())

    return all_episodes



if __name__ == '__main__':
    main()
