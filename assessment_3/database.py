from colorama import Fore
from terminaltables import AsciiTable


db = {
    "fleet": [],
    "customers": [],
    "shipments": [],
    "deliveries": [],
}

"""
Vehicle Operations
"""


def insert_vehicle(obj):
    db["fleet"].append(obj)
    print(Fore.GREEN + f"Vehicle {obj.id} added to the fleet.")


def retrieve_vehicle(id):
    for obj in db["fleet"]:
        if obj.id == id:
            return obj

    raise ValueError(Fore.RED + "No vehicles found with this ID")


def delete_vehicle(id):
    for index, obj in enumerate(db["fleet"]):
        if obj.id == id:
            db["fleet"].pop(index)
            print(Fore.GREEN + "Vehicle successfully removed from fleet")


def list_vehicles():
    """
    We defined to transform obj attributes to list
    in a method in our model.
    """
    table_data = [
        ["ID", "Type", "Capacity"],
    ]
    [table_data.append(obj.to_list()) for obj in db["fleet"]]

    table = AsciiTable(table_data)
    print(table.table)


"""
Customer Operations
"""


def insert_customer(obj):
    db["customers"].append(obj)
    print(
        Fore.GREEN + f"Customer {obj.name} with id {obj.id} was successfully created."
    )


def retrieve_customer(id):
    for obj in db["customers"]:
        if obj.id == id:
            return obj

    raise ValueError(Fore.RED + "No Customer found with this ID")


def delete_customer(id):
    for index, obj in enumerate(db["customers"]):
        if obj.id == id:
            db["customers"].pop(index)
            print(Fore.GREEN + "Customer successfully removed")


def list_customers():
    return db["customers"]


"""
Shipment Operations
"""


def insert_shipment(obj):
    db["shipments"].append(obj)
    print(Fore.GREEN + f"Shipment {obj.id} was successfully created.")


def retrieve_shipment(id):
    for obj in db["shipments"]:
        if obj.id == id:
            return obj

    raise ValueError(Fore.RED + "No Shipment found with this ID")


def list_shipments():
    return db["shipments"]


"""
Delivery Operations
"""


def insert_delivery(obj):
    db["deliveries"].append(obj)
    print(
        Fore.GREEN
        + f"Delivery of shipment {obj.shipment.id} was successfully recorded."
    )


def retrieve_delivery(shipment):
    for obj in db["deliveries"]:
        if obj.shipment.id == shipment.id:
            return obj

    raise ValueError(Fore.YELLOW + "Delivery for this shipment is still In Transit")
