#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import sys

from setuptools import find_packages, setup

from pipenv.project import Project

here = os.path.abspath(os.path.dirname(__file__))

project = Project()

about = {}
with open(os.path.join(here, 'rest_witchcraft', '__version__.py')) as f:
    exec(f.read(), about)  # yapf: disable


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), 'rb').read().decode('utf-8')


if sys.argv[-1] == 'publish':
    twine = shutil.which('twine')
    if twine is None:
        print('twine not installed.\nUse `pip install twine`.\nExiting.')
        sys.exit()
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    print('You probably want to also tag the version now:')
    print('  git tag -a %s -m %s' % (about['__version__'], about['__version__']))
    print('  git push --tags')
    os.system('make clean')
    sys.exit()

setup(
    author=about['__author__'], author_email=about['__author_email__'], description=about['__description__'],
    install_requires=project.parsed_pipfile['packages'].keys(), license='MIT', long_description=read('README.rst'),
    name=project.name, packages=find_packages(exclude=['tests']),
    url='https://github.com/shosca/django-rest-witchcraft', version=about['__version__'],
    keywords='sqlalchemy django rest framework drf rest_framework', classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
