import re
from colorama import Fore, Style


def validate_positive_integer(value):
    if not value.isdecimal() or not int(value) > 0:
        raise ValueError(Fore.RED + "Value must be a positive number")


def validate_vehicle_id(vehicle_id):
    regex = re.compile("^V[0-9]+")
    result = regex.match(vehicle_id)

    if not vehicle_id.isalnum():
        raise ValueError(Fore.RED + "Vehicle ID must be alphanumeric")

    if not result or len(result.group()) < 4:
        raise ValueError(
            Fore.RED + "Vehicle ID must be in format: VXXX (X is any number from 0-9)"
        )


def validate_object_deletion(obj):
    confirmation = (
        input(
            Fore.YELLOW
            + f"Are you sure you want to delete objcted ID {obj.id}? (y/n): "
        )
        .strip()
        .lower()
    )
    if confirmation != "y":
        raise ValueError(Fore.YELLOW + "Vehicle deletion cancelled.")

    return True

def exit_from_list_display():
    exit = ""

    while exit != "exit":
        exit = input(Fore.YELLOW + "Type 'exit' to go back to fleet menu: ")

    print(Style.RESET_ALL, end='')