import lxml
import os, argparse
from datetime import datetime, date, time, timedelta

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
lines = f.readlines()

Walters_Birthday = date(1957, 9, 7)
Walter_Turns_50 = Walters_Birthday.replace(year=Walters_Birthday.year + 50)

print 'Walt\'s birthday = ' + str(Walters_Birthday)
print 'Walt\'s 50th = ' + str(Walter_Turns_50)

print 'First calendar day in show = ' + str(Walter_Turns_50.isocalendar())