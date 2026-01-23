import uuid
from Models.Reservation import Reservations
from .user_service import User_Verwaltung
from datetime import datetime

class Reservation:

    def __init__(self):
        self.user_service = User_Verwaltung()

    def create_reservation(self, responsible_user_email, printer, start_date, end_date, start_hour, end_hour):

        printer_id = printer.id if hasattr(printer, "id") else str(printer).strip()

        if self.is_reserved(printer_id, start_date, start_hour, end_date, end_hour):
            return {"success": False, "error": "Gerät ist in diesem Zeitraum bereits reserviert"}

        if not printer_id:
            return {"success": False, "error": "Drucker ungültig"}

        if not responsible_user_email.strip():
            return {"success": False, "error": "Email darf nicht leer sein"}
        
        if start_date is None:
            return {"success": False, "error": "Startdatum darf nicht leer sein"}
        
        if end_date is None:
            return {"success": False, "error": "Enddatum darf nicht leer sein"}
        
        if start_hour is None or end_hour is None:
            return {"success": False, "error": "Uhrzeigt ungültig"}
        
        if end_hour <= start_hour and start_date == end_date:
            return{"success": False, "error": "Uhrzeit ungültig"}
        
        if end_date < start_date:
            return {"success": False, "error": "Enddatum darf nicht vor Startdatum liegen"}
        

        existing = self.user_service.get_user_by_email(responsible_user_email)
        if not existing:
            return {"success": False, "error": "User existiert nicht"}

        reservation = Reservations(
            id=str(uuid.uuid4()),
            responsible_user_email=responsible_user_email,
            printer=printer_id,
            start_hour=start_hour,
            end_hour=end_hour,
            start_date=start_date,
            end_date=end_date,
        )
        reservation.store_data()
        return {"success": True}
    
    def get_all_reservations(self):
        return Reservations.find_all()
    
    def delete_reservation(self, reservation_id: str):
        reservation = Reservations.find_by_attribute("id", reservation_id)
        if not reservation:
            return {"success": False, "error": "Reservierung nicht gefunden"}
        reservation.delete()
        return {"success": True}
    
    def is_reserved(self, printer_id, start_date, start_hour, end_date, end_hour):
        
        new_start = datetime.combine(start_date, start_hour)
        new_end   = datetime.combine(end_date, end_hour)

        for r in Reservations.find_all():
            if r.printer != printer_id:
                continue

            old_start = datetime.combine(r.start_date, r.start_hour)
            old_end   = datetime.combine(r.end_date, r.end_hour)

            if new_start < old_end and old_start < new_end:
                return True

        return False
        
    def is_reserved_now(self, printer_id: str) -> bool:
        now = datetime.now()
        for r in Reservations.find_all():
            if r.printer != printer_id:
                continue

            old_start = datetime.combine(r.start_date, r.start_hour)
            old_end   = datetime.combine(r.end_date, r.end_hour)

            if old_start <= now < old_end:
                return True

        return False