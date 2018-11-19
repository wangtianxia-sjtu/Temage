import tornado.web
from tornado.web import RequestHandler
import json


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello World")
