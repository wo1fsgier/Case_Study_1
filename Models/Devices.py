import uuid
from datetime import datetime
from Models.Serializable import Serializable
from database import Singleton
from tinydb import Query

class Device(Serializable):
    db_connector = Singleton().get_table("devices")
    def __init__(self, id: str, name:str, responsible_user_id: str, status:str  = "free", creation_date: datetime = None, last_update: datetime = None):

        super().__init__(id=id, creation_date=creation_date, last_update=last_update)         
        self.name = name
        self.status =status              
        self.responsible_user_id = responsible_user_id

    def set_status(self, new_status: str):
        self.status = new_status
        self.last_update = datetime.now()

    @classmethod
    def instantiate_from_dict(cls, data:dict)-> "Device":
        return cls(
            id=data["id"],
            name=data["name"],
            responsible_user_id=data["responsible_user_id"],
            status=data.get("status", "free"),
            creation_date=datetime.fromisoformat(data["creation_date"]),
            last_update=datetime.fromisoformat(data["last_update"]),
        )

    
    def __str__(self):
        return f"{self.name} ({self.id})"
