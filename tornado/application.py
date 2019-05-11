import tornado.web
import config
from views import index, embedding,image_match, history
import sentry_sdk
from sentry_sdk.integrations.tornado import TornadoIntegration
    
# sentry_sdk.init(
#     dsn="https://ba1972926f5b4e53ad3de8613229170d@sentry.io/1395806",
#     integrations=[TornadoIntegration()]
# )

class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            ("/", index.IndexHandler),
            ("/embedding", embedding.EmbeddingHandler),
            ("/image_match", image_match.ImageMatchHandler),
            ("/history_predict", history.HistoryHandler)
        ]
        super(Application, self).__init__(handlers, **config.settings)
        # 加入config里面的settings配置
