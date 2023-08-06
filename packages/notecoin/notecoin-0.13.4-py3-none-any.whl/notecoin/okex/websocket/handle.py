from notecoin.okex.websocket.utils import (check, get_local_timestamp, partial,
                                           update_asks, update_bids)


class BaseHandle:
    def __init__(self, channels, *args, **kwargs):
        self.channels = channels

    def solve(self, data) -> bool:
        data = eval(data)
        print(f"{get_local_timestamp()}\t{len(data)}")
        if 'event' in data:
            return False
        channel = data['args']['channel']
        if channel in self.channels:
            return self.handle(data)

    def handle(self, data) -> bool:
        pass


class PublicBooks(BaseHandle):
    def __init__(self, *args, **kwargs):
        super(PublicBooks, self).__init__(channels=['books'], *args, **kwargs)

    def handle(self, data) -> bool:
        l = []
        if data['action'] == 'snapshot':
            for m in l:
                if data['arg']['instId'] == m['instrument_id']:
                    l.remove(m)
            # 获取首次全量深度数据
            bids_p, asks_p, instrument_id = partial(data)
            d = {}
            d['instrument_id'] = instrument_id
            d['bids_p'] = bids_p
            d['asks_p'] = asks_p
            l.append(d)

            # 校验checksum
            checksum = data['data'][0]['checksum']
            # print('推送数据的checksum为:' + str(checksum))
            check_num = check(bids_p, asks_p)
            # print('校验后的checksum为:' + str(check_num))
            if check_num == checksum:
                print("校验结果为:True")
            else:
                print("校验结果为:False，正在重新订阅……")
                return False

        elif data['action'] == 'update':
            for j in l:
                if data['arg']['instId'] == j['instrument_id']:
                    # 获取全量数据
                    bids_p = j['bids_p']
                    asks_p = j['asks_p']
                    # 获取合并后数据
                    bids_p = update_bids(data, bids_p)
                    asks_p = update_asks(data, asks_p)

                    # 校验checksum
                    checksum = data['data'][0]['checksum']
                    # print('推送数据的checksum为:' + str(checksum))
                    check_num = check(bids_p, asks_p)
                    # print('校验后的checksum为:' + str(check_num))
                    if check_num == checksum:
                        print("校验结果为:True")
                    else:
                        print("校验结果为:False，正在重新订阅……")
                        return False
        return True
