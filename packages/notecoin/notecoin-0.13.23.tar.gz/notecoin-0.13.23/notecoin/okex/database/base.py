
class BaseTable(object):
    def json(self):
        res = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return res
