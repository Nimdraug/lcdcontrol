#!/usr/bin/env python2
from setuptools import setup

setup(
    name = 'lcdcontrol',
    version = '0.2',

    maintainer = u'Martin Hult\xe9n-Ashauer',
    maintainer_email = 'martin@nimdraug.com',
    url = 'http://github.com/Nimdraug/lcdcontrol',
    license = 'MIT',
    description = 'Control backlighting on a Chalkboard Electronics LCD Touch Screen',

    py_modules = [
        'lcdcontrol'
    ],
    entry_points = {
        'console_scripts': [
            'lcdcontrol = lcdcontrol:main'
        ]
    },
    install_requires = [
        'hid'
    ]
)
