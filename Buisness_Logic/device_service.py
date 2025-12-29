import uuid
from tinydb import TinyDB, Query
from Models.Devices import Device
from database import devices_table
from .user_service import User_Verwaltung


class Device_Verwaltung:

    def __init__(self):
        self.user_service = User_Verwaltung()
        self.db = TinyDB("db.json")
        self.devices = self.db.table("devices")

    def create_device(self, name, responsible_user_email):

        if not name.strip():
            return {"success": False, "error": "Name darf nicht leer sein"}

        if not responsible_user_email.strip():
            return {"success": False, "error": "Email darf nicht leer sein"}

        for u in devices_table.all():
            if u.get("name") == name:
                return {"success": False, "error": "Gerät existiert bereits"}
            
        user = self.user_service.get_user_by_email(responsible_user_email)
        if not user:
            return {"success": False, "error": "User existiert nicht"}

        device = Device(
            geraete_id=str(uuid.uuid4()),
            name=name,
            responsible_user_id=user.id
        )

        devices_table.insert(device.to_dict())
        return {"success": True}
    
    def get_user_email_for_device(self, device: Device) -> str:

        user = self.user_service.get_user_by_id(device.user_id)
        return user.email 
    
    def get_all_devices(self):
        return [
        Device.from_dict(d)
        for d in devices_table.all()
        ]

    def delete_device(self, device_id: str):
        search = Query()
        removed = devices_table.remove(search.id == device_id)
        return removed

    def update_device(self, device_id: str, data: dict):
        search = Query()
        updates = {}
        # keine leeren Felder, sonst crasht tindydb:
        if "name" in data:
            name = data["name"].strip()
            if not name: 
                return{"success": False, "error": "Name darf nicht leer sein"}
            # doppelte Namen blockieren:
            for i in devices_table.all():
                if i.get("name") == name and i.get("id") != device_id:
                    return{"success": False, "error": "Gerät exestiert bereits"}
            
            updates["name"] = name
        # User für das Gerät updaten:
        if "responsible_user_email" in data:
            email = data["responsible_user_email"].strip()
            if not email:
                return{"success": False, "error": "Email darf nicht leer sein"}
            user = self.user_service.get_user_by_email(email)
            if not user:
                return{"success": False, "error": "User exestiert nicht"}
            
            updates["responsible_user_id"] = user.id
        
        devices_table.update(updates, search.id == device_id)
        return{"success": True, "updated": updates}
    
    def change_status(self, device_id, status):
        # Das brauchen wir erst bei Reservierungen
        pass
 

