#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        pass

class SignupHandler(BaseHandler):
    def post(self):
        pass

class SigninHandler(BaseHandler):
    def post(self):
        pass

class SignoutHandler(BaseHandler):
    def get(self):
        pass



handlers = [
        (r'/', BaseHandler),
        (r'/signup', SignupHandler),
        (r'/signin', SigninHandler),
        (r'/signout', SignoutHandler),
]
