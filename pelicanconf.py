#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chirag Jain'
SITENAME = 'The Digital Paper'
SITEURL = 'http://localhost:8000'
PATH = 'content'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

FEED_DOMAIN = SITEURL

IGNORE_FILES = ['.#*', '*.pyc', '__pycache__']
THEME = "themes/perec-mod"
PLUGIN_PATHS = ['plugins']
PLUGINS = ['coming_soon']
DELETE_OUTPUT_DIRECTORY = True

SOCIAL = (
    ('github', 'https://github.com/chiragjn/'),
    ('at', 'mailto:jain.chirag925@gmail.com'),
    ('facebook', 'https://www.facebook.com/chiragjn101'),
    ('twitter', 'http://www.twitter.com/chiragjn101'),
    ('stack-overflow', 'http://stackoverflow.com/users/3697191/chiragjn'),
    ('linkedin', 'http://linkedin.com/in/chiragjn')
)

DEFAULT_METADATA = {
    'status': 'draft',
}

DEFAULT_PAGINATION = 10
ARTICLE_ORDER_BY = 'reversed-date'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
TAGLINE = "Technology and Thoughts"
STATIC_PATHS = ['images']

# Other Stuff
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
DEFAULT_CATEGORY = "General"
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 10
