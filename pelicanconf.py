#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'switch263'
SITENAME = 'getoffmyinter.net'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'atilla'
STATIC_PATHS = ['static']
#COLOR_SCHEME_CSS = 'tomorrow_night.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HEADER_COVER = 'static/fz8-warehouse-1280x960.jpg'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Photos', 'http://switch263.github.io/photos/'),
         )

# Social widget
SOCIAL = (('github', 'https://www.github.com/switch263'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

AUTHORS_BIO = {
  "switch263": {
    "name": "switch263",
    "cover": 'static/fz8-warehouse-1280x960.jpg',
    "image": "assets/images/avatar.png",
    "website": "https://switch263.github.io",
    "linkedin": "unavailable",
    "github": "switch263",
    "location": "Austin",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

MENUITEMS = (
             ('Follow me on GitHub!', 'https://github.com/switch263'),
)
