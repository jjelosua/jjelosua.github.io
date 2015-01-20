#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Juan Elosua'
SITENAME = u'Juan Elosua'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Source', 'https://source.opennews.org/en-US/'),
         ('Livia Labate', 'http://livialabate.com/'),
         ('Julia Smith', 'http://julia.nightbirdstudios.com/'),
         ('Francis Tseng', 'http://frnsys.com/'),
         ('Linda Sandvik', 'http://lindasandvik.info/'),
         ('Kavya Sukumar', 'http://kavyasukumar.com/'),
         ('Tara Adiseshan', 'http://www.taraandtheworld.com/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/jjelosua'),
          ('linkedin', 'https://es.linkedin.com/pub/juan-elosua/b/274/689'),
          ('github', 'https://github.com/jjelosua'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#WHILE TESTING
LOAD_CONTENT_CACHE = False

#THEME
THEME = 'pelican-bootstrap3'

#Disable categories on menu
DISPLAY_CATEGORIES_ON_MENU = False

#Show category on each post
SHOW_ARTICLE_CATEGORY = True

#Show author on each post
SHOW_ARTICLE_AUTHOR = True

#SIDEBAR Options
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

# About me blurb
ABOUT_ME = ''' Spanish Telecommunications engineer.<br>
               When I discovered data journalism, I became a data addict &amp; freelance developer.<br>
               OpenData &amp; Transparency enthusiast.<br>
               2015 Knight-Mozilla fellow at <a href="http://www.lanacion.com.ar/" target="_blank">La Nacion</a>
           '''
AVATAR = '/images/profile.jpg'

#Content license
CC_LICENSE = 'CC-BY-SA'

#Twitter cards
USE_OPEN_GRAPH = True
TWITTER_CARDS = True
TWITTER_USERNAME = 'jjelosua'
OPEN_GRAPH_IMAGE = ''

#FAVICON
FAVICON = 'images/favicon.png'

################## Add custom css #########################
CUSTOM_CSS = 'static/custom.css'

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/.gitignore_prod': {'path': '.gitignore'},
    'extra/custom.css':{'path':'static/custom.css'},
    'extra/README':{'path':'README.md'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extra']
