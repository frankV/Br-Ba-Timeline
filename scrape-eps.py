import lxml
import os, argparse

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