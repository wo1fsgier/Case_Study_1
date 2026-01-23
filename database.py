import os
from tinydb import TinyDB
from tinydb.table import Table
from tinydb.storages import JSONStorage
from datetime import datetime, date, time
from tinydb_serialization import Serializer, SerializationMiddleware
from tinydb_serialization.serializers import DateTimeSerializer

class Singleton:
    __instance = None
    _db = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.json')
            cls.__instance._db = TinyDB(cls.__instance.path, storage=serializer)

        return cls.__instance
    
    def get_table(self, table_name: str) -> Table:
        return self._db.table(table_name)
    
class DateSerializer(Serializer):
    # The class this serializer handles --> must be date instead of datetime.date
    OBJ_CLASS = date

    def encode(self, obj):
        return obj.isoformat()

    def decode(self, s):
        return date.fromisoformat(s)

class TimeSerializer(Serializer):
    # The class this serializer handles --> must be time instead of datetime.time
    OBJ_CLASS = time
    
    def encode(self, obj):
        return obj.isoformat()

    def decode(self, s):
        return time.fromisoformat(s)

serializer = SerializationMiddleware(JSONStorage)
serializer.register_serializer(DateTimeSerializer(), 'TinyDateTime')
serializer.register_serializer(DateSerializer(), 'TinyDate')
serializer.register_serializer(TimeSerializer(), 'TinyTime')


#%%

if __name__ == "__main__":
    db_connector = Singleton().get_table('devices')
    result = db_connector.all()

    if result:
        result = [x["device_name"] for x in result]
    
    print(result)
    