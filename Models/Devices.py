import uuid
from datetime import datetime

class Device:
    def __init__(self, name: str, geraete_id, responsible_user_id: str):

        self.id = geraete_id         
        self.name = name
        self.status = "frei"                 
        self.creation_date = datetime.now()  
        self.last_update = self.creation_date
        self.user_id = responsible_user_id

    def set_status(self, new_status: str):
        self.status = new_status
        self.last_update = datetime.now()
    
    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "status": self.status,
        "creation_date": self.creation_date.isoformat(),
        "last_update": self.last_update.isoformat(),
        "responsible_user_id": self.user_id
    }

    @staticmethod
    def from_dict(data: dict) -> "Device":
        device = Device(
            name=data["name"],
            geraete_id=data["id"],
            responsible_user_id=data["responsible_user_id"]
        )

        device.status = data["status"]
        device.creation_date = datetime.fromisoformat(data["creation_date"])
        device.last_update = datetime.fromisoformat(data["last_update"])
        return device