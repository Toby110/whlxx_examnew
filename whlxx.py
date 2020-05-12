#!/usr/bin/python
#coding=utf-8
import tornado.web
import tornado.ioloop
import asyncio
settings = {
    "static_path": "static",
   
}

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


def make_app():
    return tornado.web.Application([
        (r'/', IndexHandler),
    ], **settings)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = make_app()
    app.listen(8090)
    tornado.ioloop.IOLoop.current().start()
