#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
sys.path.append(os.curdir)

SITEURL = 'https://chiragjn.github.io/blog'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_PATH = 'github_output'

DISQUS_SITENAME = "thedigitalpaper"
GOOGLE_ANALYTICS = "UA-82047790-1"
