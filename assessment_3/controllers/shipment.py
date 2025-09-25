from terminaltables import AsciiTable

from models.shipment import Shipment
from models.vehicle import Vehicle

from utils.validators import validate_shipment


def management():
    options = {
        "3.1": "Create a new shipment",
        "3.2": "Track a shipment ",
        "3.3": "View all shipments",
        "3.4": "Quit shipment management",
    }

    print("\n--- Case Study: Shipment Management  ---")
    print("Select a task to perform:")
    [print(f"{key} - {value}") for key, value in options.items()]
    choice = input("Choose an option:")

    match choice:
        case "3.1":
            add_shipment()
            management()
        case "3.2":
            track_shipment()
            management()
        case "3.3":
            list_shipments()
            management()
        case "3.4":
            quit_shipment_management()
        case _:
            print("Invalid option")
            management()


def add_shipment():
    data = {}

    try:
        data["id"] = input("Enter Shipment ID: ").strip()
        data["origin"] = input("Enter Shipment Origin: ").strip()
        data["destination"] = input("Enter Shipment Destination: ").strip()
        data["weight"] = input("Enter Shipment Weight: ").strip()
        Vehicle.list_fleet()
        data["vehicle"] = input("Enter Shipment Transport: ").strip()

        validate_shipment(**data)

        obj = Shipment(**data)
        obj.save()

    except Exception as e:
        print(e)


def track_shipment():
    try:
        shipment = Shipment.track(input("Enter Shipment ID: ").strip())

        table_data = [["ID", "Origin", "Destination", "Status"]]
        table_data.append(
            [shipment.id, shipment.origin, shipment.destination, shipment.status]
        )
        table = AsciiTable(table_data)
        print(table.table)

    except Exception as e:
        print(e)


def list_shipments():
    table_data = [
        [
            "ID",
            "Origin",
            "Destination",
            "Weight",
            "Vehicle",
            "Status",
            "Delivery Date",
        ]
    ]

    shipments = Shipment.all()

    [table_data.append(obj.to_list()) for obj in shipments]
    table = AsciiTable(table_data)
    print(table.table)


def quit_shipment_management():
    return
