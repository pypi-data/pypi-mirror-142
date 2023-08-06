# coding=utf-8
#!/usr/bin/env python3
import json
import random
import string
import threading
import time

from logzero import logger
from paho.mqtt import client as mqtt

class EmqModel:
    """
    host: 主机
    port：端口号
    uname：用户名
    pswd：密码
    p_clientid：客户端id标识， 自动补充随机后缀
    p_flag： 传输协议， 0为tcp/ip, 1为websocket
    """
    TCPMODE = 0
    WEBSOCKET = 1
    def __init__(self, host, port, uname, pswd, p_clientid, p_flag=WEBSOCKET, sub_list=None):
        assert type(host) is str and type(port) is int and type(p_clientid) is str, "数据类型错误"
        self.host = host
        self.port = port
        self.username = uname if uname else ''
        self.password = pswd if pswd else ''
        self.clientid = p_clientid + ''.join(random.sample(string.ascii_letters + string.digits, 15))
        self.p_flag = p_flag
        self._connected = False
        self._connect_handler = None
        self._disconnect_handler = None
        self._client = None
        self._message_handler = None
        self.sub_list = sub_list if sub_list else []

    def get_status(self):
        return self._client and (self._client._state == 1)

    def on_connect(self, client, userdata, flags, rc):
        self._connected = True
        for sub in self.sub_list:
            client.subscribe(sub)
        logger.info("连接emq" + self.host + "成功")

    def on_disconnect(self, client, userdata, rc, *args):
        self._connected = False
        logger.info("" + self.host + "断开连接")

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        logger.info("收到信息：%s" % message)
        message = message.strip('\r\n')
        try:
            mjson = json.loads(message)
        except Exception as e:
            logger.error("json格式错误：" + str(e))
            return
        logger.info(mjson)

    def publish(self, topic, payload, qos=0):
        if not self._client:
            return logger.error('客户端未连接, 发布失败：' + str(payload))
        msg_info = self._client.publish(topic, payload=payload, qos=qos)
        if msg_info.rc != 0:
            logger.error('消息发布失败: ' + str(payload))
            return False
        logger.info('publish msg: topic %s, msg: %s' % (topic, str(payload)))
        return True

    def add_connect_handler(self, connect_handler):
        if callable(connect_handler):
            self._connect_handler = connect_handler

    def add_message_handler(self, message_handler):
        if callable(message_handler):
            self._message_handler = message_handler

    def add_data_handler(self, data_hander):
        if callable(data_hander):
            t = threading.Thread(target=data_hander)
            t.setDaemon(True)
            t.start()

    def add_disconnect_handler(self, disconnect_handler):
        if callable(disconnect_handler):
            self._disconnect_handler = disconnect_handler


    @property
    def is_connect(self):
        return self._client is not None

    def _client_loop(self):
        client = mqtt.Client(client_id=self.clientid, transport="tcp" if not self.p_flag else "websockets")
        self._client = client
        client.username_pw_set(username=self.username, password=self.password)
        client.on_connect = self._connect_handler if self._connect_handler else self.on_connect
        client.on_message = self._message_handler if self._message_handler else self.on_message
        client.on_disconnect = self._disconnect_handler if self._disconnect_handler else self.on_disconnect
        while True:
            try:
                client.connect(self.host, self.port, 60)
                break
            except Exception as e:
                logger.error(self.host + '连接失败')
                time.sleep(1)
        client.loop_forever()


    def run(self, daemon=True):
        t = threading.Thread(target=self._client_loop)
        t.setDaemon(daemon)
        t.start()
        return t, self._client_loop, []

