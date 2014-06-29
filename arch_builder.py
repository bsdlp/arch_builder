#!/usr/bin/env python3

import docker
from github3 import login
from getpass import getpass
import os


_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
_vol_bindings = {
    '/opt/mkimage/': {
        'bind': _SCRIPT_DIR,
        'ro': False
    }
}
username = ''
password = ''
docker_uri = 'unix://var/run/docker.sock'
repo = []

try:
    import config
    username = config.username
    docker_uri = config.docker_uri
    repo = config.repo.split('/', maxsplit=1)
except:
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

g = login(username=username, password=password,
          two_factor_callback=_two_fa_input)
repository = g.repository(repo[0], repo[1])

dc = docker.Client(base_url=docker_uri)
container = dc.create_container(image='{0}/{1}'.format(repo[0], repo[1]),
                                command='/opt/mkimage/mkimage.sh', tty=True,
                                stdin_open=True, volumes=[_SCRIPT_DIR])
dc.start_container(container=container, binds=_vol_bindings, privileged=True)
