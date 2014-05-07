import os, argparse, lxml, re
from datetime import datetime, date, time, timedelta
from bs4 import BeautifulSoup as bs4
from imdb import IMDb

""" argparse options

usage: scrape-eps.py [-h] filename

scrapes eps(episodes) from html file.

positional arguments:
  filename    file to use

optional arguments:
  -h, --help  show this help message and exit

"""
parser = argparse.ArgumentParser(
        description='scrapes eps from html file.', fromfile_prefix_chars="@" )
parser.add_argument('filename', help='file to use', action='store')
# parse arguments
args = parser.parse_args()

cwd = os.getcwd()
f = open(os.path.join(cwd, args.filename), 'r')
# lines = f.readlines()

Walters_Birthday = date(1957, 9, 7)
Walter_Turns_50 = Walters_Birthday.replace(year = Walters_Birthday.year + 50)
First_Calendar_Day = Walter_Turns_50

print 'Walt\'s birthday = ' + str(Walters_Birthday)
print 'Walt\'s 50th = ' + str(Walter_Turns_50)

print 'First calendar day in show = ' + str(Walter_Turns_50.isocalendar())

print '\n'

# season lists, 
# will hold episode data for each corresponding season
seasons = 6
season1, season2, season3, season4, season5a, season5b = ([] for i in range(seasons))

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
	sections = html.findAll('p', attrs={'class' : 'eps'})
	for section in sections:
		# print section
		if '<strong>' in str(section):
			title = section.find('strong')
			title = ''.join(title.findAll(text=True))

			# print title

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
			# print eps_season.group(0) + ", " + eps_number.group(0) + " ",
			print eps_tdelta.group(0) + '\t',



			if eps_end_date != None:
				eps_start_date = last_eps_end_date
			
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

			print "Calendar Duration: " + str(eps_start_date) + " to " + str(eps_end_date)

			# set holder for this eps end date
			last_eps_end_date = eps_end_date

# print season1







