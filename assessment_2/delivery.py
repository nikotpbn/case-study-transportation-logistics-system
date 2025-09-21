"""
0:33:38 to finish this first module
"""

from utils.util import clear_screen
from datetime import datetime

from database import mark_shipment_delivered, insert_delivery

from utils.validators import (
    validate_shipment_exists,
    validate_shipment_not_delivered,
    validate_delivery_exists,
)

from utils.util import print_delivery_date


def delivery_management():
    options = {
        "3.1": "Record delivery for a shipment",
        "3.2": "View delivery status for a shipment",
        "3.3": " Quit delivery management",
        "3.4": "Clear Screen",
    }

    [print(f"{key} - {value}") for key, value in options.items()]
    choice = input("Choose an option:")

    match choice:
        case "3.1":
            record_shipment()
            delivery_management()

        case "3.2":
            view_delivery_status()
            delivery_management()

        case "3.3":
            quit_delivery_management()

        case "3.4":
            clear_screen()
            delivery_management()


def record_shipment():
    try:
        shipment_id = input("Enter Shipment ID: ").strip()
        shipment = validate_shipment_exists(shipment_id)
        validate_shipment_not_delivered(shipment)
        mark_shipment_delivered(shipment_id)

        data = {
            "shipment": shipment_id,
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        insert_delivery(data)

    except Exception as e:
        print(e)


def view_delivery_status():
    try:
        shipment_id = input("Enter Shipment ID to check delivery: ").strip()
        delivery = validate_delivery_exists(shipment_id)
        delivery_date = datetime.strptime(delivery[1], "%Y-%m-%d %H:%M:%S")
        print_delivery_date(delivery_date)

    except Exception as e:
        print(e)


def quit_delivery_management():
    print("Exiting delivery management...")
