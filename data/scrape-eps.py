import os, argparse, re
from datetime import date, timedelta
from bs4 import BeautifulSoup as bs4


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

    print 'Walt\'s birthday = ' + str(Walters_Birthday)
    print 'Walt\'s 50th = ' + str(Walter_Turns_50)
    print 'First calendar day in show = ' + str(Walter_Turns_50.isocalendar())

    eps_start_date = First_Calendar_Day
    eps_end_date = None
    weekDelta = 0
    dayDelta = 0

    """
    parsing html

    """
    # souping
    html = bs4(f)

    # parsing
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

                print season_id.group(0) + "." + episode_id.group(0) + ":",
                print eps_title.group(0),
                print "Time Since Pilot: " + eps_tdelta.group(0) + '\t'

                ep = {}
                ep['season'] = season_id.group(0)
                ep['title'] = eps_title.group(0).replace(',', '').replace('"', '')
                ep['episode'] = episode_id.group(0)
                ep['time_since_pilot'] = eps_tdelta.group(0)

                if eps_end_date != None:
                    eps_start_date = last_eps_end_date
                    # last_eps_end_date isn't initialized (defined at the end of this
                    # function at the end of the first loop.. not sure what it's supposed to be.

                # add week delta
                if weekDelta != 0:
                    # print "add " + weekDelta.group(0) + " weeks",
                    eps_end_date = First_Calendar_Day + weekDelta

                    # reset weekDelta
                    weekDelta = 0

                # add day delta
                if dayDelta != 0:
                    # print "and " + dayDelta.group(0) + " days"
                    eps_end_date = First_Calendar_Day + dayDelta

                    # reset dayDelta
                    dayDelta = 0

                print "Dates: " + str(eps_start_date) + " to " + str(eps_end_date)

                ep['calendar_start'] = eps_start_date
                ep['calendar_end'] = eps_end_date
                print ep
                print '\n'
                all_episodes.append(ep)

                # set holder for this eps end date
                last_eps_end_date = eps_end_date

        return all_episodes


def main():
    args = parse_args()


    # season lists, will hold episode data for each corresponding season
    seasons = 6
    season1, season2, season3, season4, season5a, season5b = ([] for i in range(seasons))

    parse_html(args.filename)

if __name__ == '__main__':
    main()



