#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.web

import app

handlers = []
handlers += app.handlers
