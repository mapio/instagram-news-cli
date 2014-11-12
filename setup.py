from setuptools import setup, find_packages
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open( 'README.md', encoding = 'utf-8' ) as f:
    long_description = f.read()

setup(

    name = 'instagram-news',
    version = '0.1a',
    description = 'A command line tool to list Instagram news feeds',
    long_description = long_description,
    url = 'http://documentup.com/mapio/instagram-news',

    # Author details
    author = 'Massimo Santini',
    author_email = 'massimo.santini@unimi.it',

    # Choose your license
    license = 'GPLv3',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],

    keywords = 'instagram command line newsfeed',

    packages = find_packages(),

    entry_points={
        'console_scripts': [
            'instagram-news=instagram_news:main',
        ],
    },
)
