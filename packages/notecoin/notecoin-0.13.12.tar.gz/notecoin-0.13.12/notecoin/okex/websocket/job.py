from notecoin.okex.websocket.channel import PrivateChannel
from notecoin.okex.websocket.connect import PrivateConnect
from notetool.secret import read_secret

api_key = read_secret(cate1='coin', cate2='okex', cate3='api_key')
secret_key = read_secret(cate1='coin', cate2='okex', cate3='secret_key')
passphrase = read_secret(cate1='coin', cate2='okex', cate3='passphrase')

connect = PrivateConnect(channels=[PrivateChannel.private_positions(instType='ANY', uly=None, instId=None)],
                         api_key=api_key,
                         secret_key=secret_key,
                         passphrase=passphrase)
connect.run()
