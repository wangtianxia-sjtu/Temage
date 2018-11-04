import tornado.web
import config
from views import index


class Application(tornado.web.Application):
    def __init__(self):
        # 路由
        handlers = [
            (r"/", index.IndexHandler)
        ]
        super(Application, self).__init__(handlers, **config.settings)
        # 加入config里面的settings配置
