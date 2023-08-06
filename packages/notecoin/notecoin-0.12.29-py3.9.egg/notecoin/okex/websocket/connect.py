import base64
import hmac
import json
import logging
import time

from notecoin.okex.websocket.utils import (check, get_local_timestamp, partial,
                                           update_asks, update_bids)

from websocket import WebSocket, WebSocketException, create_connection


class BaseConnect:
    def __init__(self, url, channels, api_key=None, secret_key=None, passphrase=None):
        self.url = url
        self.channels = channels
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

        self.ws: WebSocket = create_connection(self.url)
        self.subscribe_start()

    def run(self):
        while True:
            try:
                res = self.ws.recv()
            except (TimeoutError, WebSocketException):
                try:
                    self.ping()
                except Exception as e:
                    logging.warning(f"连接关闭，正在重连:{e}")
                    self.subscribe_restart()
                continue
            self.handle_data(res)

    def handle_data(self, res):
        pass

    def ping(self):
        self.ws.send('ping')
        res = self.ws.recv()
        print(res)
        assert res == 'pong'

    def subscribe_restart(self):
        self.subscribe_stop()
        self.subscribe_start()

    def subscribe_start(self):
        self.ws: WebSocket = create_connection(self.url)
        sub_param = {"op": "subscribe", "args": self.channels}
        sub_str = json.dumps(sub_param)
        self.ws.send(sub_str)
        print(f"send: {sub_str}")
        res = self.ws.recv()
        print(f"recv: {res}")
        time.sleep(1)

    def subscribe_stop(self):
        self.ws: WebSocket = create_connection(self.url)
        sub_param = {"op": "unsubscribe", "args": self.channels}
        sub_str = json.dumps(sub_param)
        self.ws.send(sub_str)
        print(f"send: {sub_str}")
        res = self.ws.recv()
        print(f"recv: {res}")


class PublicConnect(BaseConnect):
    def __init__(self, channels, *args, **kwargs):
        super(PublicConnect, self).__init__(url="wss://ws.okx.com:8443/ws/v5/public",
                                            channels=channels, *args, **kwargs)

    def handle_data(self, res):
        res = eval(res)
        print(f"{get_local_timestamp()}\t{res}")
        if 'event' in res:
            return
        l = []
        for i in res['arg']:
            if 'books' in res['arg'][i] and 'books5' not in res['arg'][i]:
                # 订阅频道是深度频道
                if res['action'] == 'snapshot':
                    for m in l:
                        if res['arg']['instId'] == m['instrument_id']:
                            l.remove(m)
                    # 获取首次全量深度数据
                    bids_p, asks_p, instrument_id = partial(res)
                    d = {}
                    d['instrument_id'] = instrument_id
                    d['bids_p'] = bids_p
                    d['asks_p'] = asks_p
                    l.append(d)

                    # 校验checksum
                    checksum = res['data'][0]['checksum']
                    # print('推送数据的checksum为:' + str(checksum))
                    check_num = check(bids_p, asks_p)
                    # print('校验后的checksum为:' + str(check_num))
                    if check_num == checksum:
                        print("校验结果为:True")
                    else:
                        print("校验结果为:False，正在重新订阅……")
                        self.subscribe_stop()
                        self.subscribe_start()

                elif res['action'] == 'update':
                    for j in l:
                        if res['arg']['instId'] == j['instrument_id']:
                            # 获取全量数据
                            bids_p = j['bids_p']
                            asks_p = j['asks_p']
                            # 获取合并后数据
                            bids_p = update_bids(res, bids_p)
                            asks_p = update_asks(res, asks_p)

                            # 校验checksum
                            checksum = res['data'][0]['checksum']
                            # print('推送数据的checksum为:' + str(checksum))
                            check_num = check(bids_p, asks_p)
                            # print('校验后的checksum为:' + str(check_num))
                            if check_num == checksum:
                                print("校验结果为:True")
                            else:
                                print("校验结果为:False，正在重新订阅……")
                                self.subscribe_stop()
                                self.subscribe_start()


class PrivateConnect(BaseConnect):

    def __init__(self, channels, *args, **kwargs):
        super(PrivateConnect, self).__init__(url='wss://ws.okx.com:8443/ws/v5/private',
                                             channels=channels, *args, **kwargs)

    def handle_data(self, res):
        print(res)

    def subscribe_start(self):
        self.ws = create_connection(self.url)
        timestamp = str(get_local_timestamp())
        message = timestamp + 'GET' + '/users/self/verify'
        mac = hmac.new(bytes(self.secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
        sign = base64.b64encode(mac.digest()).decode("utf-8")
        login_param = {"op": "login", "args": [{"apiKey": self.api_key,
                                                "passphrase": self.passphrase,
                                                "timestamp": timestamp,
                                                "sign": sign}]}
        login_str = json.dumps(login_param)
        self.ws.send(login_str)
        print(f"send: {login_str}")


class TradeConnect(PrivateConnect):
    def __init__(self, *args, **kwargs):
        super(TradeConnect, self).__init__(*args, **kwargs)

    def handle_data(self, res):
        print(res)
