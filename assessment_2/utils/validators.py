from database import retrieve_vehicle, retrieve_shipment, retrieve_delivery
from colorama import Fore


"""
Vehicles validations
"""


def validate_vehicle_unique_id(vehicle_id):
    result = retrieve_vehicle(vehicle_id)

    if result:
        raise ValueError(Fore.RED + "Vehicle with this ID already exists.")


def validate_vehicle_exists(vehicle_id):
    result = retrieve_vehicle(vehicle_id)

    if not result:
        raise ValueError(Fore.RED + "A vehicle with this ID does not exist.")


def validate_vehicle_removal():
    confirmation = (
        input(Fore.YELLOW + "Are you sure you want to delete this vehicle? (y/n): ")
        .strip()
        .lower()
    )
    if confirmation != "y":
        raise ValueError(Fore.YELLOW + "Vehicle deletion cancelled.")

    return True


"""
Shipments validations
"""


def validate_shipment_unique_id(shipment_id):
    result = retrieve_shipment(shipment_id)

    if result:
        raise ValueError(Fore.RED + "Shipment with this ID already exists.")


def validate_shipment_exists(shipment_id):
    result = retrieve_shipment(shipment_id)

    if not result:
        raise ValueError(Fore.RED + "A shipment with this ID does not exist.")

    return result


def validate_shipment_not_delivered(shipement):
    if shipement[-1] == "Delivered":
        raise ValueError(Fore.RED + "This shipment has already been delivered.")


"""
Delivery validations
"""


def validate_delivery_exists(shipment_id):
    result = retrieve_delivery(shipment_id)

    if not result:
        raise ValueError(Fore.RED + "No delivery record found for this shipment.")

    return result


"""
General validations
"""


def validate_positive_integer(value):
    if not value.isdecimal() or not int(value) > 0:
        raise ValueError(Fore.RED + "Value must be a positive number")
