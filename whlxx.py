#!/usr/bin/python
#coding=utf-8
import tornado.web
import tornado.ioloop

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
    
    app = make_app()
    app.listen(8090)
    tornado.ioloop.IOLoop.current().start()
