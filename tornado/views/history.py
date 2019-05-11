import tornado.web
from tornado.web import RequestHandler,asynchronous
from tornado.escape import json_decode
from keras.models import load_model
import numpy as np
import jieba
import re
import copy
import json
import time
class HistoryHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')
    def initialize(self):
        self.model = load_model('./model/histories/histories.h5')
        self.data = json_decode(self.request.body)
    def post(self, *args, **kwargs):
        histories = np.array(self.data.historys)
        result = self.model.predict([histories])
        self.finish(json.dumps(result.tolist()))

        