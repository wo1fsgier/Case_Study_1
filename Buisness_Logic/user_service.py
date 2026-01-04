from Models import User
from database import users_table
from tinydb import TinyDB, Query
import uuid
from database import devices_table


class User_Verwaltung:

    def create_user(self, name, email):
    
        if not name.strip():
            return {"success": False, "error": "Name darf nicht leer sein"}
    
        if not email.strip():
            return {"success": False, "error": "Email darf nicht leer sein"}

        for u in users_table.all():
            if u.get("email") == email:
                return {"success": False, "error": "User existiert bereits"}

        user = User(
          user_id=str(uuid.uuid4()),
            name=name,
            email=email
        )

        users_table.insert(user.to_dict())
        return {"success": True}

    def get_all_users(self):

        users = []

        for u in users_table.all():
            user_obj = User.from_dict(u)
            users.append(user_obj)

        return users
    
    def get_user_by_email(self, email: str) -> User | None:
        for u in users_table.all():
            if u.get("email") == email:
                return User.from_dict(u)
        return None

    def get_user_by_id(self, user_id: str):
        for u in users_table.all():
            if u.get("id") == user_id:
                return User.from_dict(u)
        return None
    
    def delete_user(self, user_id: str):
        search = Query()
        has_devices = devices_table.contains(search.responsible_user_id == user_id)
        if has_devices:
            return{"success": False, "error": "Nutzer haftet für einen Drucker"}
        removed = users_table.remove(search.id == user_id)
        if removed:
            return{"success":True}
        else:
            return {"success":False, "error": "Nutzer nicht gefudnen"} 

    def edit_user(self, user_id: str, data: dict):
        search = Query()
        updates = {}
        # keine leeren Felder, sonst crasht tinydb:
        if "name" in data:
            name = data["name"].strip()
            if not name: 
                return{"success": False, "error": "Name darf nicht leer sein"}
            updates["name"] = name

        if "email" in data:
            email = data["email"].strip()
            if not email:
                return{"success": False, "error": "Email darf nicht leer sein"}
            exists = users_table.get(search.email == email)
            if exists and exists.get("id") != user_id:
                return{"success": False, "error": "Email exestiert bereits"}
            updates["email"] = email
    
        users_table.update(updates, search.id == user_id)
        return{"success": True, "updated": updates}