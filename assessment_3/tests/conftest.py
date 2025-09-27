import pytest


@pytest.fixture
def emails():
    return {
        "test_data": [
            "john@example.com",
            "john.doe@test.org",
            "mary_2002@example.uk",
            "jane-2001@test.pt",
            "smith@example.net",
            "smith@own-org.net",
            "ISVALID-option@example.org",
            "not_valid@test.x",
            "not$valid@example.com",
            "1nv@l1d@example.net",
        ],
        "positives": 7,
        "negatives": 3,
    }


@pytest.fixture
def customer_ids():
    """
    List of customer IDs for testing
    First five examples should be valid
    """

    return {
        "test_data": [
            "ABC001",
            "DEF123",
            "GHI456",
            "JKL789",
            "MNO012",
            "123456",
            "ABCDEF",
            "123ABC",
            "346DEF",
            "ABCD12",
            "AB1234",
            "AB123",
            "ABC12",
            "ABDC1234",
            "1234ABCD",
        ],
        "positives": 5,
        "negatives": 10,
    }


@pytest.fixture
def addresses():
    return {
        "test_data": [
            "234 Main St, Sydney, NSW 2000, Australia",
            "Main St 234, Sydney, NSW 2000, Australia",
            "Sydney, Main St 234, NSW 2000, Australia",
            "Main St 234, Sydney, 2000 NSW, Australia",
            "Australia, Main St 234, Sydney, NSW 2000",
            "Main St 234, Sydney, Australia, NSW 2000",
        ],
        "positives": 1,
        "negatives": 5,
    }


@pytest.fixture
def numbers():
    return {
        "test_data": [
            "0412345678",
            "0487654321",
            "041234567",
            "04123456789",
            "0212345678",
            "0512345678",
            "AB12345678",
            "12345678AB",
            "1234AB5678",
        ],
        "positives": 2,
        "negatives": 7,
    }
