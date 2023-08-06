import logging

from notecoin.database.base import create_all, session
from notecoin.okex.websocket.dataset import OkexSocketPublicTickers
from notecoin.okex.websocket.utils import get_local_timestamp


class BaseHandle:
    def __init__(self, channels, *args, **kwargs):
        self.channels = channels

    def solve(self, data) -> bool:
        data = eval(data)
        print(f"{get_local_timestamp()}\t{len(data)}")
        if 'event' in data:
            return False
        if 'args' not in data or 'channel' not in data['args']:
            logging.info(data)

        channel = data['args']['channel']
        if channel in self.channels:
            return self.handle(data)

    def handle(self, data) -> bool:
        print(f"{data['args']['channel']}:{len(str(data))}")
        return True


class PublicTickers(BaseHandle):
    def __init__(self, *args, **kwargs):
        create_all()
        super(PublicTickers, self).__init__(channels=['tickers'], *args, **kwargs)

    def handle(self, data) -> bool:
        try:
            for arg in data['data']:
                session.merge(OkexSocketPublicTickers(**arg))
                session.commit()
        except Exception as e:
            logging.error(f"error:{e}")
            return False
        return True
