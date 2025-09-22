from colorama import init
from controllers.fleet import management as fleet_management

init(autoreset=True)


def main_menu():
    options = {
        "1": "Fleet Management",
        "2": "Customer Management",
        "3": "Shipment Management",
        "4": "Delivery Management",
        "0": " Quit Application",
    }
    print("\n--- Case Study: Transportation Logistics System  ---")
    print("Select a task to perform:")
    [print(f"{key} - {value}") for key, value in options.items()]
    choice = input("Choose an option:")

    match choice:
        case "1":
            fleet_management()
        # case "2":
        #     shipment_management()
        # case "3":
        #     delivery_management()
        case "0":
            quit_application()
        case _:
            print("Invalid option")
            main_menu()


def quit_application():
    print("Quitting Application")
    exit()


if __name__ == "__main__":
    while True:
        main_menu()
