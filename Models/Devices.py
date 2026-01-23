from datetime import date
from Models.Serializable import Serializable
from database import Singleton

class Device(Serializable):
    db_connector = Singleton().get_table("devices")
    def __init__(self, id: str, name:str, responsible_user_id: str, status:str  = "free",service_cost: float=0.0, service_intervall: float=0, last_update: date = None):

        super().__init__(id=id, last_update=last_update)
        self.name = name
        self.status =status              
        self.responsible_user_id = responsible_user_id
        self.service_cost = service_cost
        self.service_intervall = service_intervall

    def set_status(self, new_status: str):
        
        self.status = new_status
        self.last_update = date.today()

    @classmethod
    def instantiate_from_dict(cls, data:dict)-> "Device":
        return cls(
            id=data["id"],
            name=data["name"],
            responsible_user_id=data["responsible_user_id"],
            status=data.get("status", "free"),
            last_update=data.get("last_update"),
            service_cost=data.get("service_cost"),
            service_intervall=data.get("service_intervall")
        )

    def __str__(self):
        return f"{self.name} ({self.id})"
