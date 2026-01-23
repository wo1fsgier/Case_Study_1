import uuid
from Models.Devices import Device
from .user_service import User_Verwaltung
from .reservation_service import Reservation
from datetime import date


class Device_Verwaltung:

    def __init__(self):
        self.user_service = User_Verwaltung()
        self.reservation_service = Reservation()

    def create_device(self, name, responsible_user_email, service_cost, service_intervall):

        if not name.strip():
            return {"success": False, "error": "Name darf nicht leer sein"}
        
        try:
            service_cost = float(service_cost)
        except (TypeError, ValueError):
            return {"success": False, "error": "Servicekosten müssen eine Zahl sein"}

        try:
            service_intervall = int(service_intervall)
        except (TypeError, ValueError):
            return {"success": False, "error": "Serviceintervall muss eine ganze Zahl sein"}

        if not responsible_user_email.strip():
            return {"success": False, "error": "Email darf nicht leer sein"}

        existing = Device.find_by_attribute("name", name)
        if existing:
            return {"success": False, "error": "Gerät existiert bereits"}
            
        user = self.user_service.get_user_by_email(responsible_user_email)
        if not user:
            return {"success": False, "error": "User existiert nicht"}

        device = Device(
            id=str(uuid.uuid4()),
            name=name,
            responsible_user_id=user.id,
            service_intervall=service_intervall,
            service_cost=service_cost,
            last_update=date.today(),
        )
        device.store_data()
        return {"success": True}

    
    def get_user_email_for_device(self, device: Device) -> str:

        user = self.user_service.get_user_by_id(device.responsible_user_id)
        return user.email if user else ""
    
    def get_all_devices(self):
        return Device.find_all()

    def delete_device(self, device_id: str):
        device = Device.find_by_attribute("id", device_id)
        removed = device.delete()
        return removed

    def update_device(self, device_id: str, data: dict):
        device = Device.find_by_attribute("id", device_id)
        updates = {}
        # keine leeren Felder, sonst crasht tindydb:
        if "name" in data:
            new_name = data["name"].strip()
            if not new_name: 
                return{"success": False, "error": "Name darf nicht leer sein"}
            
            
            if Device.find_by_attribute("name", new_name) and (Device.find_by_attribute("name", new_name)).id != device_id:
                return{"success": False, "error": "Gerät exestiert bereits"}
            device.name = new_name
            updates["name"] = new_name
        
        # User für das Gerät updaten:
        if "responsible_user_email" in data:
            email = data["responsible_user_email"].strip()
            if not email:
                return{"success": False, "error": "Email darf nicht leer sein"}
            user = self.user_service.get_user_by_email(email)
            if not user:
                return{"success": False, "error": "User exestiert nicht"}
            
            updates["responsible_user_id"] = user.id
        
            device.responsible_user_id = user.id
        device.store_data()
        return{"success": True, "updated": updates}
    
    def user_has_devices(self, user_id: str) -> bool:
        return Device.find_by_attribute("responsible_user_id", user_id) is not None

    
    def get_status(self, device) -> str:
        return "busy" if self.reservation_service.is_reserved_now(device.id) else "free"