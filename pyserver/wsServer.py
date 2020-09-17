from typing import Any

import tornado.websocket
import tornado.web
import tornado.ioloop
import getIp

from tornado import httputil

from controller import changeAxisPercentage
class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    connect_users = set()
    def __init__(self, application: tornado.web.Application, request: httputil.HTTPServerRequest, **kwargs: Any):
        super().__init__(application, request, **kwargs)
        self.byteType = type(b"")

    def check_origin(self, origin: str):
        '''重写同源检查 解决跨域问题'''
        return True

    def open(self):
        print("WebSocket connected "+self.request.host)
        # 打开连接时将用户保存到connect_users中
        self.connect_users.add(self)

    def solveStrMessage(self, message):
        print(message)


    def on_message(self, message):

        messageType = type(message)
        if messageType != self.byteType:
            #处理str消息
            self.solveStrMessage(message)
            return
        #处理bytestring消息
        # print(int(message))
        changeAxisPercentage("X",int(message))

    def on_close(self):
        print("WebSocket closed")
        # 关闭连接时将用户从connect_users中移除
        self.connect_users.remove(self)

    @classmethod
    def send_demand_updates(cls, message):
        # 使用@classmethod可以使类方法在调用的时候不用进行实例化
        # 给所有用户推送消息（此处可以根据需要，修改为给指定用户进行推送消息）
        for user in cls.connect_users:
            user.write_message(message)


class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r'/ws', MyWebSocketHandler)
        ]
        tornado.web.Application.__init__(self, handlers)
        print("websocket listening")
import tornado.platform.asyncio
        # asyncio.set_event_loop_policy(tornado.platform.asyncio.AnyThreadEventLoopPolicy())
app = Application()
app.listen(20482)
tornado.ioloop.IOLoop.current().start()
