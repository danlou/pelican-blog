#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan Lou'
SITENAME = 'Dan Lou'
SITEURL = 'http://localhost:8000'


PATH = 'content'
THEME = 'pelican-hyde'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

BIO = 'Hello World!'
PROFILE_IMAGE = 'profile_pic.jpg'

# Social widget
SOCIAL = (('email', 'daniel.b.loureiro@gmail.com'),
          ('github', 'http://github.com/danlou'),
          ('twitter', 'http://twitter.com/danielbloureiro'),
          ('linkedin', 'http://www.linkedin.com/in/danielloureiro/'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
