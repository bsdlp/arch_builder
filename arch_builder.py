#!/usr/bin/env python3

from github3 import login
from getpass import getpass


username = ''
password = ''
repo = []

try:
    import config
    username = config.username
    repo = config.repo.split('/', maxsplit=1)
except ImportError:
    pass

while not username:
    username = input('GitHub Username: ')

while not password:
    password = getpass('Password for {0}: '.format(username))

while not repo:
    repo = input('GitHub Repo (i.e. fly/arch): ').split('/', maxsplit=1)

def _two_fa_input():
    two_fa = ''
    while not two_fa:
        two_fa = input('Two Factor Code: ')
    return two_fa

g = login(username=username, password=password, two_factor_callback=_two_fa_input)

repository = g.repository(repo[0], repo[1])
