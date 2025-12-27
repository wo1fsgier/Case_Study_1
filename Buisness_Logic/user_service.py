from Models import User
from database import users_table
import tinydb as tdb
import uuid

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
    

