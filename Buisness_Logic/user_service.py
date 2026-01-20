from Models.User import User
from Models.Devices import Device
import uuid
from database import Singleton


class User_Verwaltung:
    def __init__(self):
        pass

    def create_user(self, name, email):
    
        if not name.strip():
            return {"success": False, "error": "Name darf nicht leer sein"}
    
        if not email.strip():
            return {"success": False, "error": "Email darf nicht leer sein"}

        if User.find_by_attribute("email", email):
            return{"success": False, "error": "User existiert bereits"}

        user = User(
          id=str(uuid.uuid4()),
            name=name,
            email=email
        )

        user.store_data()
        return {"success": True}

    def get_all_users(self):
        return User.find_all()
    
    def get_user_by_email(self, email: str) -> User | None:
        return User.find_by_attribute("email", email)

    def get_user_by_id(self, user_id: str):
        return User.find_by_attribute("id", user_id)
    
    def delete_user(self, user_id: str):
        user = User.find_by_attribute("id", user_id)
        has_devices = Device.find_by_attribute("responsible_user_id", user_id) is not None
        if has_devices:
            return{"success": False, "error": "Nutzer haftet für einen Drucker"}
        user.delete()
        return{"success":True}
       

    def edit_user(self, user_id: str, data: dict):
        user = User.find_by_attribute("id", user_id)
        updates = {}
        # keine leeren Felder, sonst crasht tinydb:
        if "name" in data:
            name = data["name"].strip()
            if not name: 
                return{"success": False, "error": "Name darf nicht leer sein"}
            user.name = name

        if "email" in data:
            email = data["email"].strip()
            if not email:
                return{"success": False, "error": "Email darf nicht leer sein"}
            exists = User.find_by_attribute("email", email)
            if exists and exists.id != user_id:
                return{"success": False, "error": "Email exestiert bereits"}
            user.email = email
    
        user.store_data()
        return {"success": True}