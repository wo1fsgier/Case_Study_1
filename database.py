import os
from tinydb import TinyDB
from tinydb.table import Table




class Singleton:
    __instance = None
    _db = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.json')
            cls.__instance._db = TinyDB(cls.__instance.path)
        return cls.__instance
    
    def get_table(self, table_name: str) -> Table:
        return self._db.table(table_name)