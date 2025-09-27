from utils.validators import validate_shipment_id, validate_positive_integer


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


def test_shipment_id_regex(shipments):
    validate_data(
        shipments["test_data"],
        validate_shipment_id,
        shipments["positives"],
        shipments["negatives"],
    )


def test_positive_interger(integers):
    validate_data(
        integers["test_data"],
        validate_positive_integer,
        integers["positives"],
        integers["negatives"],
    )
