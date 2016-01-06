from __future__ import print_function
from fabric.api import *  # noqa


@task
def build(dirname, autopush=True):
    with lcd(dirname):
        image_tag = 'registry.guangzixuexi.com/thematrix/' + dirname
        local('docker build -t ' + image_tag + ' .')
        local('docker push ' + image_tag)
