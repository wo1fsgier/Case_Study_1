class device_service:

    def create_device():

        ##Hier später weiterarbeiten :)
        '''
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
'''
        pass
    
    def get_all_devices():
        
        pass

    def delete_device(device_id):

        pass

    def update_device(device_id, data):

        pass

    def change_status(device_id, status):
        
        pass


