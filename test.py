#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from prowl import Prowl

APIKEY = os.environ['APIKEY']

prowl = Prowl(APIKEY)
prowl.add('application', 'event', 'description', 0, 'https://example.com')
