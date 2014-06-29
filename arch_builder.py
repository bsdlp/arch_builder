#!/usr/bin/env python3

from github3 import login
from getpass import getpass

username = ''
password = ''

while not username:
    username = input('GitHub Username: ')

while not password:
    password = getpass('Password for {0}: '.format(username))

def _two_fa_input():
    two_fa = ''
    while not two_fa:
        two_fa = input('Two Factor Code: ')
    return two_fa

g = login(username=username, password=password, two_factor_callback=_two_fa_input)
