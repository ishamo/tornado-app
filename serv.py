#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado
from tornado.ioloop

import route

def main():
    application = tornado.web.Application(
            route.handlers,
            )
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()


