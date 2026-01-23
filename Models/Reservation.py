from Models.Serializable import Serializable
from database import Singleton

class Reservations(Serializable):
    db_connector = Singleton().get_table("reservation")
    def __init__(self, id, responsible_user_email, printer, start_date, end_date, start_hour, end_hour):
        
        super().__init__(id=id)
        self.responsible_user_email = responsible_user_email
        self.printer = printer
        self.start_date = start_date
        self.end_date = end_date
        self.start_hour = start_hour
        self.end_hour = end_hour
    
    @classmethod
    def instantiate_from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            responsible_user_email=data["responsible_user_email"],
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            printer=data.get("printer"),
            start_hour=data.get("start_hour"),
            end_hour=data.get("end_hour")
            
        )
    def __str__(self):
        return f"{self.id} ({self.id})"