from typing import Self
from datetime import date
from Models.Serializable import Serializable
from database import Singleton

class Wartung(Serializable):
    db_connector = Singleton().get_table("wartung")

    def __init__(
        self, id: str, printer: str, responsible_user_email: str, service_date: date, costs: float, last_update=None):
        super().__init__(id=id)

        self.printer = printer
        self.responsible_user_email = responsible_user_email
        self.service_date = service_date
        self.costs = costs

    @classmethod
    def instantiate_from_dict(cls, data: dict) -> Self:
        return cls(
            id=data.get("id"),
            printer=data.get("printer"),
            responsible_user_email=data.get("responsible_user_email", ""),
            service_date=data.get("service_date"),
            costs=data.get("costs", 0.0),
            last_update=data.get("last_update"),
        )

    def __str__(self):
        return f"Wartung({self.printer}) am {self.service_date} – {self.costs} €"
