from fabric.api import *


def test():
    local( 'coverage run manage.py test && coverage report' )
