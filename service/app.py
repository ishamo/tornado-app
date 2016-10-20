#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user():
        pass


class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')

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


class EntityHandler(BaseHandler):
    def get(self):
        pass


class ArchiveHandler(BaseHandler):
    def get(self):
        pass


class AtomHandler(BaseHandler):
    def get(self):
        pass


handlers = [
        (r'/', BaseHandler),
        (r'/signup', SignupHandler),
        (r'/signin', SigninHandler),
        (r'/signout', SignoutHandler),
]
