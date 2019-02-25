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
from keras.preprocessing.image import load_img, img_to_array

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
    @gen.coroutine
    def prepare(self):
        self.dimension = 1024
        self.sentence_length = 2
        self.embedding = Embedder('./model/elmo/zhs.model/')
        self.target_size = (224, 224)
        self.file_path = '' 

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
    
    @run_on_executor 
    def predict(self, image, embedings):
        model = load_model('./model/text_image/')
        img = load_img(image,target_size=self.target_size)
        img = img_to_array(img)
        img /= 255
        length = embedings.shape(0)
        imgs = []
        for i in range(length):
            imgs.append(img)
        result = model.predict([np.array(imgs, embedings)])
        return result
    
    @asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        file_metas = self.request.files.get('file', None)
        if not file_metas:
            self.write(json.dumps({'msg': 'no files', 'code': 400}))
        else:
            data = json_decode(self.request.body)
            text_array = data['text_array']
            sentences_embeddings = yield [self.get_embedding(item) for item in text_array]
            file_metas = self.request.files.get('file', None)
            file_paths = []
            for meta in file_metas:
                file_path = self.file_path + meta['filename']
                with open(file_path, 'wb') as up:
                    up.write(meta['body'])
                file_paths.append(file_path)
            sentences_embeddings = np.array(sentences_embeddings).reshape((-1, self.dimension*self.sentence_length, 1))
            results = yield [self.predict(path, sentences_embeddings) for path in file_paths]
            
        