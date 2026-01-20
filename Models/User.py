from typing import Self
from Models.Serializable import Serializable
from database import Singleton

class User(Serializable):
    db_connector = Singleton().get_table("users")
    def __init__(self, id, email:str, name:str, creation_date=None, last_update = None):
        
        super().__init__(id, creation_date, last_update)
        self.name = name
        self.email = email
        
    @classmethod
    def instantiate_from_dict(cls, data:dict) -> Self:
        return cls(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            creation_date=data.get("creation_date"),
            last_update=data.get("last_update"),
        )
    
    def __str__(self):
        return f"{self.name} ({self.id})"
