from datetime import date, timedelta
from .device_service import Device_Verwaltung
from Models.Maintainance import Wartung

class maintenance:
    def __init__(self):
        self.device_service = Device_Verwaltung()

    def get_maintenance_overview(self) -> list[dict]:
        devices = self.device_service.get_all_devices()
        today = date.today()
        
        maintenance_today = set()
        for w in Wartung.find_all():
            sd = getattr(w, "service_date", None)
            if sd is None:
                continue
            if hasattr(sd, "date"):
                sd = sd.date()
            if sd == today:
                maintenance_today.add(getattr(w, "printer", None))

        rows = []
        
        for d in devices:
            locked_today = d.id in maintenance_today
            lu = getattr(d, "last_update", None) 
            service_intervall = int(getattr(d, "service_intervall", 0) or 0)
            next_m = (lu + timedelta(days=service_intervall)) if (lu and service_intervall > 0) else None
            rows.append({
                "device_id": d.id,
                "device_name": getattr(d, "name", str(d)),
                "status": getattr(d, "status", "free"),
                "locked_today": locked_today,
                "service_cost": float(getattr(d, "service_cost", 0.0) or 0.0),
                "service_intervall": int(getattr(d, "service_intervall", 0) or 0),
                "last_maintenance": lu,
                "next_maintenance": next_m, 
            })

        return rows


    def get_costs_per_quarter(self) -> dict:
        costs = {}

        for w in Wartung.find_all():
            sd = getattr(w, "service_date", None)

            q = (sd.month - 1) // 3 + 1
            quarter = f"Q{q} {sd.year}"

            cost = float(getattr(w, "costs", 0.0) or 0.0)
            costs[quarter] = costs.get(quarter, 0.0) + cost

        return costs
