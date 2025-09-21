"""
1:28:00 to finish this first Part
Not clear in assessment where status goes
thus added it to shipment table.
"""

from terminaltables import AsciiTable

from fleet import view_all_vehicles

from database import insert_shipment, list_shipments

from utils.validators import (
    validate_positive_integer,
    validate_shipment_unique_id,
    validate_vehicle_exists,
    validate_shipment_exists,
)

from utils.util import clear_screen, print_shipment_status


def shipment_management():
    options = {
        "2.1": "Create a new shipment",
        "2.2": " Track a shipment",
        "2.3": " View all shipments",
        "2.4": " Quit shipment management",
        "2.5": " Clear Screen",
    }

    [print(f"{key} - {value}") for key, value in options.items()]
    choice = input("Choose an option:")

    match choice:
        case "2.1":
            create_shipment()
            shipment_management()
        case "2.2":
            track_shipment()
            shipment_management()
        case "2.3":
            view_all_shipments()
            shipment_management()
        case "2.4":
            quit_shipment_management()
        case "2.5":
            clear_screen()
            shipment_management()
        case _:
            print("Invalid option")
            shipment_management()


def create_shipment():
    data = {
        "id": "",
        "origin": "",
        "destination": "",
        "weight": "",
        "vehicle": "",
        "status": "In transit",
    }
    try:
        # Get vehicle details from user
        data["id"] = input("Enter Shipment ID: ").strip()
        data["origin"] = input("Enter Shipment Origin: ").strip()
        data["destination"] = input("Enter Shipment Destination: ").strip()
        data["weight"] = input("Enter Shipment Weight: ").strip()

        # Validate inputs
        validate_positive_integer(data["id"])
        validate_shipment_unique_id(data["id"])
        validate_positive_integer(data["weight"])

        view_all_vehicles()
        data["vehicle"] = input("Select a Vehicle: ").strip()
        validate_vehicle_exists(data["vehicle"])

        insert_shipment(data)

    except Exception as e:
        print(e)

    shipment_management()


def track_shipment():
    try:
        shipment_id = input("Enter Shipment ID to track: ").strip()
        shipment = validate_shipment_exists(shipment_id)
        print_shipment_status(shipment[-1])

    except Exception as e:
        print(e)


def view_all_shipments():
    table_data = [
        ["ID", "Origin", "Destination", "Weight", "Vehicle", "Status"],
    ]
    shipments_list = list_shipments()
    for shipment in shipments_list:
        table_data.append(list(shipment))

    table = AsciiTable(table_data)
    print(table.table)


def quit_shipment_management():
    print("Exiting shipment management...")
