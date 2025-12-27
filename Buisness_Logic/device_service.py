from Models.Devices import Device
from .user_service import User_Verwaltung
from database import devices_table
import tinydb as tdb
import uuid


##Hier muss noch fertig implementiert werden

class Device_Verwaltung:

    def __init__(self):
        self.user_service = User_Verwaltung()

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
    
    def get_all_devices():
        
        pass

    def delete_device(device_id):

        pass

    def update_device(device_id, data):

        pass

    def change_status(device_id, status):
        
        pass


