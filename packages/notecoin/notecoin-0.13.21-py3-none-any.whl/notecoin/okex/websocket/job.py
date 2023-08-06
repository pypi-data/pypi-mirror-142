import logging

from notecoin.okex.websocket.channel import PublicChannel
from notecoin.okex.websocket.connect import PublicConnect
from notecoin.okex.websocket.handle import PublicTickers
from notetool.secret import read_secret

uri = "mysql+pymysql://notecoin:notecoin@127.0.0.1:3306/zff?charset=utf8",
# uri = f'sqlite:///{os.path.abspath(os.path.dirname(__file__))}/notecoin.db'
read_secret(cate1='notecoin', cate2='dataset', cate3='db_path', value=uri)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

connect = PublicConnect([PublicChannel.public_tickers().to_json()])
# connect.add_handle(BaseHandle("tickers"))
connect.add_handle(PublicTickers())
connect.run()
