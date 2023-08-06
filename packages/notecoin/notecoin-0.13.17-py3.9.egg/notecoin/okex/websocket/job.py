from notecoin.okex.websocket.connect import PublicConnect
from notecoin.okex.websocket.handle import BaseHandle

connect = PublicConnect('tickets')
connect.add_handle(BaseHandle("tickers"))
connect.run()
