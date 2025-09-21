"""
2:06:38 to finish this first Part
With testing and some extra features
"""

from terminaltables import AsciiTable

from database import (
    insert_vehicle,
    list_vehicles,
    update_vehicle,
    delete_vehicle,
    retrieve_vehicle,
)

from utils.validators import (
    validate_positive_integer,
    validate_vehicle_unique_id,
    validate_vehicle_removal,
)

from utils.util import clear_screen


def fleet_management():
    options = {
        "1.1": "Add a vehicle",
        "1.2": " Update vehicle information",
        "1.3": " Remove a vehicle",
        "1.4": " View all vehicles",
        "1.5": " Quit fleet management",
        "1.6": "Clear Screen",
    }

    [print(f"{key} - {value}") for key, value in options.items()]
    choice = input("Choose an option:")

    match choice:
        case "1.1":
            add_vehicle()
        case "1.2":
            update_vehicle_information()
        case "1.3":
            remove_vehicle()
        case "1.4":
            view_all_vehicles()
            fleet_management()
        case "1.5":
            quit_fleet_management()
        case "1.6":
            clear_screen()
            fleet_management()
        case _:
            print("Invalid option")
            fleet_management()


def add_vehicle():
    """
    Function to add a vehicle to the fleet
    Extra validation on ID to ensure its a number as per database convention
    (we could use an UUID but this is a simple system after all)
    """
    data = {"id": "", "type": "", "capacity": ""}

    try:
        # Get vehicle details from user
        data["id"] = input("Enter Vehicle ID: ").strip()
        data["type"] = input("Enter Vehicle Type: ").strip()
        data["capacity"] = input("Enter Vehicle Capacity: ").strip()

        # Validate inputs
        validate_positive_integer(data["id"])
        validate_positive_integer(data["capacity"])
        validate_vehicle_unique_id(data["id"])

        insert_vehicle(data)

    except Exception as e:
        print(e)

    fleet_management()


def update_vehicle_information():
    """
    Function to update vehicle information
    """
    data = {"id": "", "type": "", "capacity": ""}

    try:
        # Get vehicle ID to update
        data["id"] = input("Enter Vehicle ID to update: ").strip()

        # Try to find vehicle with given ID
        retrieve_vehicle(data["id"])

        # Get new values for type and capacity
        data["type"] = input("Enter Vehicle New Type: ").strip()
        data["capacity"] = input("Enter Vehicle New Capacity: ").strip()

        # Validate capacity to ensure a positive integer
        validate_positive_integer(data["capacity"])

        update_vehicle(data)

    except Exception as e:
        print(e)

    fleet_management()


def remove_vehicle():
    """
    Function to remove a vehicle from the fleet
    """

    data = {"id": "", "type": "", "capacity": ""}

    try:
        # Get vehicle ID to remove
        data["id"] = input("Enter Vehicle ID to remove: ").strip()

        # Validations
        retrieve_vehicle(data["id"])
        validate_vehicle_removal()

        delete_vehicle(data["id"])

    except Exception as e:
        print(e)

    fleet_management()


def view_all_vehicles():
    table_data = [
        ["ID", "Type", "Capacity"],
    ]
    vehicle_list = list_vehicles()
    [table_data.append([obj[0], obj[1], obj[2]]) for obj in vehicle_list]

    table = AsciiTable(table_data)
    print(table.table)


def quit_fleet_management():
    print("Quitting Fleet Management...")
