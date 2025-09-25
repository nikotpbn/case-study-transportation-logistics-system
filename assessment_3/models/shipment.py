from colorama import Fore

from database import insert_shipment, retrieve_shipment, list_shipments


class Shipment:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.origin = kwargs.get("origin")
        self.destination = kwargs.get("destination")
        self.weight = kwargs.get("weight")
        self.vehicle = kwargs.get("vehicle")
        self.status = "In Transit"
        self.delivery_date = "In Transit"

    def save(self):
        insert_shipment(self)

    def mark_delivered(self):
        self.status = "Delivered"
        print(Fore.GREEN + f"Shipment {self.id} marked as Delivered")

    def to_list(self):
        return [
            self.id,
            self.origin,
            self.destination,
            self.weight,
            self.vehicle,
            self.status,
            self.delivery_date,
        ]

    @classmethod
    def track(cls, id):
        return retrieve_shipment(id)

    @classmethod
    def all(cls):
        return list_shipments()
