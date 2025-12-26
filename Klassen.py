import uuid
from datetime import datetime

class User:

    def __init__(self, username, email, userid):
        self.username = username
        self.email = email
        self.userid = userid
    

class Device:
    def __init__(self, name: str, farbe: str):
        self.id = str(uuid.uuid4())          
        self.name = name
        self.farbe = farbe

        self.status = "frei"                 
        self.creation_date = datetime.now()  
        self.last_update = self.creation_date

    def set_status(self, new_status: str):
        self.status = new_status
        self.last_update = datetime.now()
    
    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "farbe": self.farbe,
        "status": self.status,
        "creation_date": self.creation_date.isoformat(),
        "last_update": self.last_update.isoformat(),
    }

    