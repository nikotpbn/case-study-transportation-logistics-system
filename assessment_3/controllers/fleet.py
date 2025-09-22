"""
1:36:24 for this one so far
+ 0:25:45 + 0:35:15
remodeling with tests
"""

from models.vehicle import Vehicle
from utils.validators import (
    validate_positive_integer,
    validate_vehicle_id,
    validate_object_deletion,
    exit_from_list_display,
)


def management():
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
            management()
        case "1.2":
            update_vehicle()
            management()
        case "1.3":
            remove_vehicle()
            management()
        case "1.4":
            list_vehicles()
            management()
        case "1.5":
            quit_fleet_management()
        #     case "1.6":
        #         clear_screen()
        #         fleet_management()
        case _:
            print("Invalid option")
            management()


def add_vehicle():
    data = {"id": "", "type": "", "capacity": ""}

    try:
        # Get vehicle details from user
        data["id"] = input("Enter Vehicle ID: ").strip()
        Vehicle.vehicle_type_menu()
        data["type"] = input("Enter Vehicle Type: ").strip()
        data["capacity"] = input("Enter Vehicle Capacity: ").strip()

        # Validate Data
        validate_vehicle_id(data["id"])
        validate_positive_integer(data["capacity"])

        # Create object and validate inputs
        obj = Vehicle(**data)
        obj.save()

    except Exception as e:
        print(e)


def update_vehicle():
    data = {"type": "", "capacity": ""}
    try:
        vehicle_id = input("Enter Vehicle ID: ").strip()
        obj = Vehicle.exists_in_fleet(vehicle_id)

        Vehicle.vehicle_type_menu()
        data["type"] = input("Enter Vehicle Type: ").strip()
        Vehicle.is_valid_vehicle_type(data["type"])

        data["capacity"] = input("Enter Vehicle Capacity: ").strip()
        validate_positive_integer(data["capacity"])

        obj.update(**data)

    except Exception as e:
        print(e)


def remove_vehicle():
    try:
        vehicle_id = input("Enter Vehicle ID: ").strip()
        obj = Vehicle.exists_in_fleet(vehicle_id)

        if validate_object_deletion(obj):
            obj.delete()

    except Exception as e:
        print(e)


def list_vehicles():
    Vehicle.list_fleet()
    exit_from_list_display()


def quit_fleet_management():
    return
