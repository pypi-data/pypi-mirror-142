import logging

from notecoin.okex.websocket.channel import PublicChannel
from notecoin.okex.websocket.connect import PublicConnect
from notecoin.okex.websocket.handle import BaseHandle

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

connect = PublicConnect([PublicChannel.public_tickers().to_json()])
connect.add_handle(BaseHandle("tickers"))
connect.run()
