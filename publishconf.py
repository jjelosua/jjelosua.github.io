#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.juanelosua.com'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

#Add RSS feed
SOCIAL = SOCIAL + (('rss', SITEURL + '/' + FEED_ALL_RSS),)

DELETE_OUTPUT_DIRECTORY = True

##################### Exterior Services ############################
#Disqus config
DISQUS_SITENAME = "juanelosua"
DISQUS_SHORTNAME = "juanelosua"
DISQUS_DISPLAY_COUNTS = True

#Google analytics config
GOOGLE_ANALYTICS = "UA-36653643-1"

#AddThis config
ADDTHIS_PROFILE = 'ra-54be57212f2a8571'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False

