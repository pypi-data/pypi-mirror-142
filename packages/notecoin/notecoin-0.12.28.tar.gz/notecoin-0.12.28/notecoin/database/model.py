import os

from notedrive.tables.core import SqliteTable
from notetool import read_secret


class KlineDetail(SqliteTable):
    def __init__(self, table_name='symbol_info', db_path=None, *args, **kwargs):
        if db_path is None:
            db_path = os.path.abspath(
                os.path.dirname(__file__)) + '/data/coin.db'

        super(KlineDetail, self).__init__(db_path=db_path, table_name=table_name,                                          *args, **kwargs)

        self.columns = ['coid_id', 'ts', 'count', 'open', 'close', 'low', 'high', 'vol', 'amount']

    def create(self):
        self.execute("""
                create table if not exists `{}` (
                `coid_id`     VARCHAR(20)	--COMMENT '交易对'
                ,`ts`         BIGINT(32)  --COMMENT '调整新加坡时间的时间戳'
                ,`count`      INT(32)     --COMMENT '交易次数'
                ,`open`       FLOAT   --COMMENT '本阶段开盘价'
                ,`close`      float   --COMMENT '本阶段收盘价'
                ,`low`	      float   --COMMENT '本阶段最低价'
                ,`high`	      float   --COMMENT '本阶段最高价'
                ,`vol`        float   --COMMENT '以报价币种计量的交易量'
                ,`amount`     float   --COMMENT '以基础币种计量的交易量'
                ,primary key (`coid_id`,`ts`)           
                      );
                    """.format(self.table_name))

    def select_all(self):
        """
        返回全表数据
        """
        return self.select("select * from table_name")

    def select(self, sql=None, condition: dict = None):
        """
        根据sql或者指定条件选择数据
        :param sql: sql
        :param condition: 条件
        :return: 记录list
        """
        if sql is None:
            equal2 = self._condition2equal(condition)
            sql = """select * from {} where {}""".format(self.table_name, ' and '.join(equal2))
        else:
            sql = self.sql_format(sql)

        rows = self.execute(sql)
        print(rows)
        return [] if rows is None else [dict(zip(self.columns, row)) for row in rows]
