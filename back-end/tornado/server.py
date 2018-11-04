import tornado.web
import tornado.ioloop
import tornado.httpserver
import config
from application import Application


if __name__ == "__main__":
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    httpServer.bind(config.options["port"]) 
    httpServer.start(1)
    # 没参数则默认开启一个进程；
    # 值大于0，创建对应个数的子进程
    # 值为None或小于0，开启对应硬件机器的cpu核心数个子进程（双核两进程）

    tornado.ioloop.IOLoop.current().start()
