import logging
import os

from notecoin.okex.websocket.channel import PublicChannel
from notecoin.okex.websocket.connect import PublicConnect
from notecoin.okex.websocket.handle import BaseHandle, PublicTickers
from notetool.secret import read_secret

uri = f'sqlite:///{os.path.abspath(os.path.dirname(__file__))}/notecoin.db'
read_secret(cate1='notecoin', cate2='dataset', cate3='db_path', value=uri)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

connect = PublicConnect([PublicChannel.public_tickers().to_json()])
# connect.add_handle(BaseHandle("tickers"))
connect.add_handle(PublicTickers())
connect.run()
