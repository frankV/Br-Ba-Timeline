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
Walter_Turns_50 = Walters_Birthday.replace(year=Walters_Birthday.year + 50)

print 'Walt\'s birthday = ' + str(Walters_Birthday)
print 'Walt\'s 50th = ' + str(Walter_Turns_50)

print 'First calendar day in show = ' + str(Walter_Turns_50.isocalendar())

print '\n'

# season lists, 
# will hold episode data for each corresponding season
seasons = 6
season1, season2, season3, season4, season5a, season5b = ([] for i in range(seasons))


"""
parsing html

"""
# souping
html = bs4(f)

# parsing
if html.find('div', attrs={'class' : 'parbase section entrytext'}):
	sections = html.findAll('div', attrs={'class' : 'parbase section entrytext'})
	for section in sections:
		# print section
		if '<strong>' in str(section):
			title = section.find('strong')
			title = ''.join(title.findAll(text=True))

			# print title

			eps_title = re.search(r'\"(.+?)\"', title)
			eps_season = re.search(r'(Season [0-9]+)', title)
			eps_number = re.search(r'(Episode [0-9]+)', title)
			eps_tdelta = re.search(r'\((.*?)\)', title)

			eps_tdeltaWeek = re.search(r'([0-9]+ week?)', str(eps_tdelta.group(0)))
			# s = str(eps_tdeltaWeek)
			# eps_tdeltaWeek = [for s in str.split() if s.isdigit()]

			eps_tdeltaDay = re.search(r'([0-9]+ day?)', str(eps_tdelta.group(0)))

			print eps_title.group(0)
			print eps_season.group(0) + ", " + eps_number.group(0)
			print eps_tdelta.group(0) + ", ",
			if eps_tdeltaWeek != None:
				print eps_tdeltaWeek.group(0) + " ",
			if eps_tdeltaDay != None: 
				print eps_tdeltaDay.group(0)
			print '\n'

# print season1







