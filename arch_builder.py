from github3 import login
from getpass import getpass

username = ''
password = ''
two_fa = ''

while not username:
    username = input('GitHub Username: ')

while not password:
    password = getpass('Password for {0}: '.format(user))

def _two_fa_input():
    while not two_fa:
        two_fa = input('Two Factor Code: ')

gh_login = login(username=username, password=password, two_factor_callback=two_fa_input)
