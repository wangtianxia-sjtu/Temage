from elmoformanylangs import Embedder
import numpy as np
e = Embedder('./zhs.model/')

sents = [['今', '天', '天气', '真', '好', '啊'],
['潮水', '退', '了', '就', '知道', '谁', '沒', '穿', '裤子']]
# the list of lists which store the sentences 
# after segment if necessary.

print(np.array(e.sents2elmo(sents)[1]).shape)
# will return a list of numpy arrays 
# each with the shape=(setence_num, words_num, embedding_size)