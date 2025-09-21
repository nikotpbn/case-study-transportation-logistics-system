import os

from colorama import Fore


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_shipment_status(status):
    status_map = {
        "In transit": "🚚 In transit",
        "Delivered": "📦 Delivered",
        "Delayed": "⏰ Delayed",
    }
    print(Fore.GREEN + "Shipment Status: " + status_map.get(status, "Unknown Status"))


def print_delivery_date(delivery_date):
    print(
        Fore.GREEN
        + f"This delivery was made on {delivery_date.strftime("%Y-%m-%d")} at {delivery_date.strftime("%H:%M:%S")}"
    )
