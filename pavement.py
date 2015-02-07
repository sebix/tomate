#!/bin/env python

from paver.easy import needs, path, sh
from paver.setuputils import install_distutils_tasks
from paver.tasks import task

install_distutils_tasks()

ROOT_PATH = path(__file__).dirname().abspath()

TOMATE_PATH = ROOT_PATH / 'tomate'


@needs(['test'])
@task
def default():
    pass


@task
def clean():
    sh('pyclean tomate')


@task
@needs(['clean'])
def test(options):
    sh('nosetests --with-coverage --cover-erase --cover-package=%s' % TOMATE_PATH)


@task
def docker_rmi():
    sh('docker rmi --force eliostvs/python-tomate', ignore_error=True)


@task
def docker_build():
    sh('docker build -t eliostvs/python-tomate .')


@task
def docker_run():
    sh('docker run --rm -v $PWD:/code eliostvs/python-tomate')


@task
@needs(['docker_rmi', 'docker_build', 'docker_run'])
def docker_test():
    pass
