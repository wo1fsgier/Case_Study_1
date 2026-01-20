import uuid
from datetime import datetime
from Models.Serializable import Serializable
from database import Singleton
from tinydb import Query

class Reservations(Serializable):
    db_connector = Singleton().get_table("users")
    def __init__(self, id, email, name:str, start_date=None, end_date = None):
        
        super().__init__(id, start_date, end_date)
        self.name = name
        self.email = email