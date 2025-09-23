"""
Customer module without shipments and no testing
took 1:38:48

For a cleaner code one can move validators
inside the object which would be according
to the DRY principle. Although its implemented
this way for assessment flow.
"""

from models.customer import Customer
from terminaltables import AsciiTable

from utils.validators import (
    validate_customer_id,
    validate_dob,
    is_of_age,
    validate_australian_address,
    validate_customer_phone_number,
    validate_customer_email_address,
)


def management():
    options = {
        "2.1": "Add a customer",
        "2.2": "Update customer information",
        "2.3": "Remove a customer",
        "2.4": "View all customers",
        "2.5": "View a customer's shipments",
        "2.6": "Quit customer management.",
    }

    [print(f"{key} - {value}") for key, value in options.items()]
    choice = input("Choose an option:")

    match choice:
        case "2.1":
            add_customer()
            management()
        case "2.2":
            update_customer()
            management()
        case "2.3":
            remove_customer()
            management()
        case "2.4":
            list_customers()
            management()
        # case "2.5":
        #     quit_fleet_management()
        case "2.6":
            quit_fleet_management()
        case _:
            print("Invalid option")
            management()


def add_customer():
    data = {"id": "", "type": "", "capacity": ""}

    try:
        # Prompt the user to enter unique Customer ID (e.g., ABC123)
        data["id"] = input("Enter Customer ID: ").strip()
        data["name"] = input("Enter Customer Name: ")
        data["dob"] = input("Enter Customer Date of Birth: ").strip()  # DD/MM/YYYY
        data["address"] = input("Enter Customer Address: ")
        data["phone_number"] = input("Enter Customer Phone Number: ").strip()
        data["email"] = input("Enter Customer Email: ").strip()

        validate_customer_id(data["id"])
        year_of_birth = validate_dob("dob")
        is_of_age(year_of_birth)
        validate_australian_address(data["address"])
        validate_customer_phone_number(data["phone_number"])
        validate_customer_email_address(data["email"])

        obj = Customer(**data)
        obj.save()

    except Exception as e:
        print(e)


def update_customer():
    data = {}
    try:
        customer = Customer.exists(input("Enter Customer ID: ").strip())

        data["name"] = input("Enter Customer Name: ")
        data["dob"] = input("Enter Customer Date of Birth: ").strip()
        data["address"] = input("Enter Customer Address: ")
        data["phone_number"] = input("Enter Customer Phone Number: ").strip()
        data["email"] = input("Enter Customer Email: ").strip()

        year_of_birth = validate_dob("dob")
        is_of_age(year_of_birth)
        validate_australian_address(data["address"])
        validate_customer_phone_number(data["phone_number"])
        validate_customer_email_address(data["email"])

        customer.update(**data)

    except Exception as e:
        print(e)


def remove_customer():
    data = {}

    try:
        customer = Customer.exists(input("Enter Customer ID: ").strip())
        customer.delete()

    except Exception as e:
        print(e)


def list_customers():
    table_data = ["ID", "Name", "Address", "Number", "Email"]

    customers = Customer.all()

    [table_data.append(obj.to_list()) for obj in customers]
    table = AsciiTable(table_data)
    print(table.table)


def quit_fleet_management():
    return
