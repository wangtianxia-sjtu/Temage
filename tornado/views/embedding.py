import tornado.web
from tornado.web import RequestHandler
from tornado.escape import json_decode
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from model.elmo.elmoformanylangs import Embedder
from tornado import gen
import jieba
import re
import copy
import json
import numpy as np
class EmbeddingHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')
    def initialize(self):
        self.sentence_vector = 1024
        self.min_length = 20
    
    def get_words_embedding(self, words_cut):
        embedding = Embedder('./model/elmo/zhs.model/')
        #embedding_result是一个m*x*1024的矩阵，第一个代表句子数量，第二个是具体某个句子的单词数量，第三个是每个单词的维度
        embedding_result = embedding.sents2elmo(words_cut)
        result = []
        for index, sentence in enumerate(embedding_result):
            if index >= self.min_length:
                break
            result.append(np.mean(sentence, axis=0).tolist())
        return np.array(result)
        
    def post(self, *args, **kwargs):
        #with the shape=(setence_num, words_num, embedding_size)
        data = json_decode(self.request.body)
        text = data['text']
        article = []
        sentences = re.split('(。|！|\!|？|\?|[…]+)', text)# 保留分割符
        l = int(len(sentences)/2)
        print(l)
        for i in range(int(l)):
            sent = sentences[2*i]
            result = jieba.lcut(sent,cut_all=False)
            article.append(copy.deepcopy(result))
        
        # 20 * 1024
        embedding_result = self.get_words_embedding(article)
        words_len = len(embedding_result)
        
        if words_len > self.min_length:
            embedding_result = embedding_result[:self.min_length]
        print(embedding_result.shape)
        embedding_result = embedding_result.reshape(1, embedding_result.shape[0], embedding_result.shape[1], 1)
        print(embedding_result.shape)
        embedding_result = embedding_result.tolist() 
        while words_len < self.min_length:
            embedding_result[0].append([0 for x in range(self.sentence_vector)])
            words_len += 1
        self.write(json.dumps(embedding_result, ensure_ascii=False))
