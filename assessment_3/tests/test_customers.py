import pytest
from datetime import datetime, timedelta
from utils.validators import (
    validate_customer_email_address,
    validate_customer_id,
    is_of_age,
    validate_australian_address,
    validate_customer_phone_number,
)


def validate_data(data, validation_function, positives, negatives):
    """
    Test a callback validation function
    """
    valid = []
    invalid = []

    for obj in data:
        try:
            validation_function(obj)
            valid.append(True)

        except Exception as e:
            print(obj)
            invalid.append(False)

    assert len(valid) == positives
    assert len(invalid) == negatives


def test_customer_email_regex(emails):
    validate_data(
        emails["test_data"],
        validate_customer_email_address,
        emails["positives"],
        emails["negatives"],
    )


def test_customer_id_regex(customer_ids):
    validate_data(
        customer_ids["test_data"],
        validate_customer_id,
        customer_ids["positives"],
        customer_ids["negatives"],
    )


def test_is_of_age_validator():
    current_year = datetime.now().year
    dates = [current_year - 15, current_year - 18]
    validations = []

    for yob in dates:
        try:
            is_of_age(yob)
            validations.append(True)
        except Exception as e:
            validations.append(False)

    assert validations[1] == True
    assert validations[0] == False


def test_validate_australian_address_regex(addresses):
    validate_data(
        addresses["test_data"],
        validate_australian_address,
        addresses["positives"],
        addresses["negatives"],
    )


def test_validate_customer_phone_number_regex(numbers):
    validate_data(
        numbers["test_data"],
        validate_customer_phone_number,
        numbers["positives"],
        numbers["negatives"],
    )
