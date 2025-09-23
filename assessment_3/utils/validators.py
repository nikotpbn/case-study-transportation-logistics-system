import re
from datetime import datetime, date
from colorama import Fore, Style


"""
General Validators
"""


def validate_positive_integer(value):
    if not value.isdecimal() or not int(value) > 0:
        raise ValueError(Fore.RED + "Value must be a positive number")


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

    print(Style.RESET_ALL, end="")


"""
Vehicle Validators
"""


def validate_vehicle_id(vehicle_id):
    regex = re.compile("^V[0-9]+")
    result = regex.match(vehicle_id)

    if not vehicle_id.isalnum():
        raise ValueError(Fore.RED + "Vehicle ID must be alphanumeric")

    if not result or len(result.group()) < 4:
        raise ValueError(
            Fore.RED + "Vehicle ID must be in format: VXXX (X is any number from 0-9)"
        )


"""
Customer Validators
"""


def validate_customer_id(customer_id):
    regex = re.compile("[A-Z]{3}[0-9]{3}")
    result = regex.match(customer_id)

    if not customer_id.isalnum():
        raise ValueError(Fore.RED + "Customer ID must be alphanumeric")

    if not result or len(result.group()) < 6:
        raise ValueError(
            Fore.RED
            + "Customer ID must be in format: AAAXXX (A is any alphabet from A-Z and X is any number from 0-9) "
        )


def validate_dob(dob):
    regex = re.compile("[0-9]{2}/[0-9]{2}/[0-9]{4}")
    result = regex.match(dob)

    if not result or len(result) != 12:
        raise ValueError(
            Fore.RED + "Date of birth should be in the following format: DD/MM/YYYY"
        )

    d = datetime.strptime(dob, "%d\/%m\/%Y").date()
    if d >= date(1920, 1, 1):
        return d.year

    raise ValueError(Fore.RED + "Date is not valid")


def is_of_age(yob):
    current_year = datetime.now().year

    if current_year - yob < 18:
        raise ValueError(Fore.RED + "Customer must be at leasst 18 years old")


def validate_australian_address(email):
    """
    51 Jacobson St
    BRISBANE QLD 4000
    """
    clean_email = email.replace(",", "")

    to_validate = clean_email.strip()
    regex = re.compile("[0-9]+[a-zA-Z]+[0-9]{4}$")
    result = regex.match(to_validate)

    if not result:
        raise ValueError(Fore.RED + "This address is not valid")

    return clean_email


def validate_customer_phone_number(phone_number):
    regex = re.compile("04[0-9]+")
    result = regex.match(phone_number)

    if not phone_number.isdigit():
        raise ValueError(Fore.RED + "Phone number must be numeric")

    if not result or len(result) != 10:
        raise ValueError(Fore.RED + "Phone number must have 10 digits")


def validate_customer_email_address(value):
    """
    A very simple email regex that validates the address
    is all lower case. It accepts numbers and three special
    characters in the first part.

    IMPORTANT: everything must be casted to lower case.

    Test Example:
    emails = ["john@example.com",
    "john.doe@test.org",
    "mary_2002@example.uk",
    "jane-2001@test.pt",
    "smith@example.net",
    "smith@own-org.net",
    "not_valid@test.x",
    "not$valid@example.com",
    "1nv@l1d@example.net"]
    for email in emails:
        return True if regex.match(email) else False
    """
    regex = re.compile("[a-z0-9._-]+@[a-z]+\\.[a-z]{2,3}")
    result = regex.match(value)

    if not result:
        raise ValueError(Fore.RED + "This email address is invalid")
