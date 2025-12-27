
class User:

    def __init__(self, user_id, email, name):
        self.name = name
        self.email = email
        self.id = user_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
    
    @staticmethod
    def from_dict(data):
        return User(
            user_id=data["id"],
            name=data["name"],
            email=data["email"]
        )