from notecoin.database.base import db


class BaseTable(object):
    def json(self):
        res = {}
        res.update(self.__dict__)
        for key in res.keys():
            if key.startswith("_"):
                res.pop(key)
        return res


class OkexSocketPublicTickers(db.Model,BaseTable):
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
        self.last = kwargs.get("last", 0)
        self.lastSz = kwargs.get("lastSz", 0)
        self.askPx = kwargs.get("askPx", 0)
        self.askSz = kwargs.get("askSz", 0)
        self.bidPx = kwargs.get("bidPx", 0)

        self.bidSz = kwargs.get("bidSz", 0)
        self.open24h = kwargs.get("open24h", 0)
        self.high24h = kwargs.get("high24h", 0)
        self.low24h = kwargs.get("low24h", 0)
        self.volCcy24h = kwargs.get("volCcy24h", 0)

        self.vol24h = kwargs.get("vol24h", 0)
        self.sodUtc0 = kwargs.get("sodUtc0", 0)
        self.sodUtc8 = kwargs.get("sodUtc8", 0)
        self.ts = kwargs.get("ts", 0)

    def __repr__(self):
        return f"instType{self.instType},instId:{self.instId}"
