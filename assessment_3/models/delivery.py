from colorama import Fore
from datetime import datetime

from database import insert_delivery, retrieve_delivery


class Delivery:
    def __init__(self, shipment):
        self.status = "Delivered"
        self.shipment = shipment
        self.timestamp = datetime.now()

    def save(self):
        insert_delivery(self)

    @classmethod
    def is_concluded(cls, shipment):
        return retrieve_delivery(shipment)
