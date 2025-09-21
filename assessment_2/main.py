from fleet import fleet_management
from shipment import shipment_management
from delivery import delivery_management

from database import create_tables

from colorama import init

init(autoreset=True)


def main_menu():
    options = {
        "1": "Fleet Management",
        "2": "Shipment Management",
        "3": "Delivery Management",
        "4": " Quit Application",
    }
    print("\n--- Case Study: Transportation Logistics System  ---")
    print("Select a task to perform:")
    [print(f"{key} - {value}") for key, value in options.items()]
    choice = input("Choose an option:")

    match choice:
        case "1":
            fleet_management()
        case "2":
            shipment_management()
        case "3":
            delivery_management()
        case "4":
            quit_application()
        case _:
            print("Invalid option")
            main_menu()


def quit_application():
    print("Quitting Application")
    exit()


if __name__ == "__main__":
    create_tables()

    while True:
        main_menu()
