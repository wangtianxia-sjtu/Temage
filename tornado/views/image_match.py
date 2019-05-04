import tornado.web
from tornado.web import RequestHandler,asynchronous
from tornado.escape import json_decode
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from model.elmo.elmoformanylangs import Embedder
from tornado import gen
import numpy as np
import jieba
import re
import copy
import json
import time
from keras.models import load_model
from keras.models import Model
from keras.optimizers import SGD
from keras import layers
from keras.preprocessing.image import load_img, img_to_array
import os
from keras import backend as K

class ImageMatchHandler(RequestHandler):
    executor = ThreadPoolExecutor(10)
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')
    
    def initialize(self):
        self.sentence_length = 2
        K.clear_session()
    @gen.coroutine
    def prepare(self):
        self.dimension = 1024
        self.sentence_length = 2
        self.embedding = Embedder('./model/elmo/zhs.model/')
        self.target_size = (224, 224)
        self.file_path = 'files'
        model_path = './model/text_image_match/text_image_all.h5'
        self.model = load_model(model_path)
        self.compare_dimension = 128 
        self.sentence_length = 2

    @run_on_executor 
    def get_embedding(self, words):
        words_cut = []
        print(words)
        for i in range(self.sentence_length):
            result = jieba.lcut(words[i],cut_all=False)
            words_cut.append(copy.deepcopy(result))
        # embedding_result是一个sentence_length*x*1024的矩阵，第一个代表句子数量，第二个是具体某个句子的单词数量，第三个是每个单词的维度
        embedding_result = self.embedding.sents2elmo(words_cut)
        result = []
        for sentence in embedding_result:
            result.append(np.mean(sentence, axis=0).tolist())
        return result
    
    def predict(self, image, embedings):
        # lstm branch for dealing with text
        img = load_img(image,target_size=self.target_size)
        img = img_to_array(img)
        img /= 255
        length = embedings.shape[0]
        imgs = []
        for i in range(length):
            imgs.append(img)
        result = self.model.predict([np.array(embedings), np.array(imgs)])
        return result
    
    @asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        file_metas = self.request.files.get('files', None)
        print("request")
        print(self.request)
        # print("request-file")
        # print(self.request.files)
        if not file_metas:
            self.write(json.dumps({'msg': 'no files', 'code': 400}))
        else:
            
            text_array = self.get_body_argument('text_array')
            print("text_array: " + text_array)
            text_array = json_decode(text_array)
            sentences_embeddings = yield [self.get_embedding(item) for item in text_array]
            file_metas = self.request.files.get('files', None)
            file_paths = []
            for meta in file_metas:

                file_path = os.path.join(self.file_path, meta['filename'])
                file_path = os.path.abspath(file_path)
                file_path = file_path.replace('\\', '/')
                with open(file_path, 'wb') as up:
                    up.write(meta['body'])
                file_paths.append(file_path)
            sentences_embeddings = np.array(sentences_embeddings).reshape((-1, self.dimension*self.sentence_length, 1))
            results =  [self.predict(path, sentences_embeddings).tolist() for path in file_paths]
            order = []
            for result in results:
                order.append(result.index(max(result)))
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            self.write(json.dumps({'order': order}))
            self.finish()
            
        