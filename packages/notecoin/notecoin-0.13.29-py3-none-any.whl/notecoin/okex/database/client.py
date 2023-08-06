from notecoin.database.base import Base, BaseTable
from sqlalchemy import BIGINT, Column, Float, String


class OkexClientAccountBalance(Base, BaseTable):
    __tablename__ = 'okex_client_account_balance'
    ccy = Column(String(120), comment='币种', primary_key=True)
    eq = Column(Float(), comment='币种总权益', primary_key=True)
    cashBal = Column(Float(), comment='币种余额')
    uTime = Column(Float(), comment='币种余额信息的更新时间毫秒')
    isoEq = Column(Float(), comment='币种逐仓仓位权益')
    availEq = Column(Float(), comment='可用保证金')
    disEq = Column(Float(), comment='美金层面币种折算权益')
    availBal = Column(Float(), comment='可用余额')
    frozenBal = Column(Float(), comment='币种占用金额')
    ordFrozen = Column(Float(), comment='挂单冻结数量')
    liab = Column(Float(), comment='币种负债额')
    upl = Column(Float(), comment='未实现盈亏')
    uplLiab = Column(Float(), comment='由于仓位未实现亏损导致的负债')
    crossLiab = Column(Float(), comment='币种全仓负债额')
    isoLiab = Column(Float(), comment='币种逐仓负债额')
    mgnRatio = Column(Float(), comment='保证金率')
    interest = Column(Float(), comment='计息')
    twap = Column(Float(), comment='当前负债币种触发系统自动换币的风险')
    maxLoan = Column(Float(), comment='币种最大可借')
    eqUsd = Column(Float(), comment='币种权益美金价值')
    notionalLever = Column(Float(), comment='币种杠杆倍数')
    stgyEq = Column(Float(), comment='策略权益')
    isoUpl = Column(Float(), comment='逐仓未实现盈亏')

    ts = Column(BIGINT(), comment='数据产生时间，Unix时间戳的毫秒数格式')

    def __init__(self, *args, **kwargs):
        self.ccy = kwargs.get("ccy")
        self.eq = kwargs.get("eq", "")
        self.cashBal = kwargs.get("cashBal", 0)
        self.isoEq = kwargs.get("isoEq", 0)
        self.availEq = kwargs.get("availEq", 0)
        self.disEq = kwargs.get("disEq", 0)
        self.availBal = kwargs.get("availBal", 0)

        self.frozenBal = kwargs.get("frozenBal", 0)
        self.ordFrozen = kwargs.get("ordFrozen", 0)
        self.liab = kwargs.get("liab", 0)
        self.upl = kwargs.get("upl", 0)
        self.uplLiab = kwargs.get("uplLiab", 0)

        self.crossLiab = kwargs.get("crossLiab", 0)
        self.isoLiab = kwargs.get("isoLiab", 0)
        self.mgnRatio = kwargs.get("mgnRatio", 0)
        self.interest = kwargs.get("interest", 0)

        self.twap = kwargs.get("twap", 0)
        self.maxLoan = kwargs.get("maxLoan", 0)
        self.eqUsd = kwargs.get("eqUsd", 0)
        self.notionalLever = kwargs.get("notionalLever", 0)
        self.stgyEq = kwargs.get("stgyEq", 0)
        self.isoUpl = kwargs.get("isoUpl", 0)

    def __repr__(self):
        return f"ccy{self.ccy},availBal:{self.availBal}"
