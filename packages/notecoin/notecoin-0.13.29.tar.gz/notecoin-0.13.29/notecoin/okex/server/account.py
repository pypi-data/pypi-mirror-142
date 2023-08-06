import pandas as pd
from notebuild.tool.fastapi import add_api_routes, api_route
from notecoin.database.connect import RedisConnect
from notecoin.okex.client.const import account_api


class AccountAccount(RedisConnect):
    def __init__(self, prefix="/account", cache_prefix='okex_account_balance', *args, **kwargs):
        super(AccountAccount, self).__init__(prefix=prefix, cache_prefix=cache_prefix, *args, **kwargs)
        add_api_routes(self)

    @api_route('/update', description="update market tickers")
    def update_value(self, suffix=""):
        data = account_api.get_account().data[0]['details']
        self.put_value(self.get_key(suffix=suffix), data)
        return {"success": len(data)}

    @api_route('/read', description="read market tickers")
    def get_value(self, suffix=""):
        return super(AccountAccount, self).get_value(suffix=suffix)


data = account_api.get_account().data[0]['details']
for detail in data:
    print(detail)
