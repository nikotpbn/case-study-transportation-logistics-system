import re
from colorama import Fore
from terminaltables import AsciiTable

from database import insert_vehicle, list_vehicles, retrieve_vehicle, delete_vehicle


class Vehicle:
    vehicle_types = {
        "1": "Truck",
        "2": "Van",
        "3": "Car",
    }

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id")
        self.type = kwargs.get("type")
        self.capacity = kwargs.get("capacity")

        # Replace vehicle choice by its name
        self.type = self.get_vehicle_name(self.type)

    def save(self):
        insert_vehicle(self)

    def update(self, *args, **kwargs):
        self.type = self.get_vehicle_name(kwargs["type"])
        self.capacity = kwargs["capacity"]

        print(Fore.GREEN + "Instance updated successfully")

    def delete(self):
        delete_vehicle(self.id)

    def to_list(self):
        return [self.id, self.type, self.capacity]

    @classmethod
    def list_fleet(cls):
        list_vehicles()

    @classmethod
    def exists_in_fleet(cls, vehicle_id):
        try:
            obj = retrieve_vehicle(vehicle_id)
            return obj
        except Exception as e:
            print(e)

    @classmethod
    def is_valid_vehicle_type(cls, choice):
        for key, value in cls.vehicle_types.items():
            if choice == key:
                return

        raise ValueError(Fore.RED + "There is no such vehicle option...")

    @classmethod
    def vehicle_type_menu(cls, *args, **kwargs):
        table_data = [
            ["Option", "Type"],
        ]
        [table_data.append([key, value]) for key, value in cls.vehicle_types.items()]
        table = AsciiTable(table_data)
        print(table.table)

    @classmethod
    def get_vehicle_name(cls, choice, *args, **kwargs):
        for key, value in cls.vehicle_types.items():
            if choice == key:
                return value
