#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tornado
from tornado.ioloop

from service import route

def main():
    application = tornado.web.Application(
            handlers = route.handlers,
            template_path = os.path.join(os.path.dirname(__file__), 'template'),
            static_path = os.path.join(os.path.dirname(__file__), 'static'),
            debug = True
            )
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    main()



