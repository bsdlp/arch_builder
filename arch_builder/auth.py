from github3 import login
from getpass import getpass

username = ''
password = ''

while not username:
    username = input('GitHub Username: ')

while not password:
    password = getpass('Password for {0}: '.format(user))

def two_fa_input():
    two_fa = ''
    while not two_fa:
        input('Two Factor Code: ')

auth = login(username=username, password=password, two_factor_callback=two_fa_input)
