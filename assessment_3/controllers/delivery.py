import sys

from terminaltables import AsciiTable

from models.shipment import Shipment
from models.delivery import Delivery


def management():
    options = {
        "4.1": "Mark Shipment delivery",
        "4.2": "View delivery status for a shipment",
        "4.3": "Quit delivery management",
    }
    print("\n--- Case Study: Delivery Management  ---")
    print("Select a task to perform:")
    [print(f"{key} - {value}") for key, value in options.items()]
    choice = input("Choose an option:")

    match choice:
        case "4.1":
            mark_shipment_delivery()
            management()
        case "4.2":
            view_delivery_status_of_shipment()
            management()
        case "4.3":
            quit_delivery_management()
        case _:
            print("Invalid option")
            management()


def mark_shipment_delivery():
    """
    We could use atomic transactions for this action since
    it works more than one model at a time that would refer
    to two tables operations in a database.
    """
    data = {}
    try:
        data["id"] = input("Enter Shipment ID: ").strip()
        shipment = Shipment.track(data["id"])

        delivery = Delivery(shipment)

        shipment.mark_delivered()
        delivery.save()

    except Exception as e:
        print(e)


def view_delivery_status_of_shipment():
    data = {}
    try:
        data["id"] = input("Enter Shipment ID: ").strip()
        shipment = Shipment.track(data["id"])

        delivery = Delivery.is_concluded(shipment)

        table_data = [["ID", "Timestamp"]]
        table_data.append([delivery.shipment.id, delivery.timestamp])

        table = AsciiTable(table_data)
        print(table.table)

    except Exception as e:
        print(e)


def quit_delivery_management():
    return
