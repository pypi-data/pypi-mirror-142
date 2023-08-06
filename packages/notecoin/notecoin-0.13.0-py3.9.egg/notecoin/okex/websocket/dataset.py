from notecoin.database.base import db


class OkexSocketPublicTickers(db.Model, object):
    instType = db.Column(db.String(120), comment='产品类型', primary_key=True)
    instId = db.Column(db.String(120), comment='产品ID', primary_key=True)

    last = db.Column(db.Float(), comment='最新成交价')
    lastSz = db.Column(db.Float(), comment='最新成交的数量')

    askPx = db.Column(db.Float(), comment='卖一价')
    askSz = db.Column(db.Float(), comment='卖一价对应的量')
    bidPx = db.Column(db.Float(), comment='买一价')
    bidSz = db.Column(db.Float(), comment='买一价对应的量')

    open24h = db.Column(db.Float(), comment='24小时开盘价')
    high24h = db.Column(db.Float(), comment='24小时最高价')
    low24h = db.Column(db.Float(), comment='24小时最低价')
    volCcy24h = db.Column(db.Float(), comment='24小时成交量，以计价货币为单位')
    vol24h = db.Column(db.Float(), comment='24小时成交量，以交易货币为单位')

    sodUtc0 = db.Column(db.Float(), comment='UTC 0时开盘价')
    sodUtc8 = db.Column(db.Float(), comment='UTC+8时开盘价')

    ts = db.Column(db.BIGINT(), comment='数据产生时间，Unix时间戳的毫秒数格式')

    def __init__(self, *args, **kwargs):
        self.instType = kwargs.get("instType", "SPOT")
        self.instId = kwargs.get("instId", "")
        self.last = kwargs.get("last", "")
        self.lastSz = kwargs.get("lastSz", "")
        self.askPx = kwargs.get("askPx", "")
        self.askSz = kwargs.get("askSz", "")
        self.bidPx = kwargs.get("bidPx", "")

        self.bidSz = kwargs.get("bidSz", "")
        self.open24h = kwargs.get("open24h", "")
        self.high24h = kwargs.get("high24h", "")
        self.low24h = kwargs.get("low24h", "")
        self.volCcy24h = kwargs.get("volCcy24h", "")

        self.vol24h = kwargs.get("vol24h", "")
        self.sodUtc0 = kwargs.get("sodUtc0", "")
        self.sodUtc8 = kwargs.get("sodUtc8", "")
        self.ts = kwargs.get("ts", "")

    def __repr__(self):
        return f"instType{self.instType},instId:{self.instId}"
