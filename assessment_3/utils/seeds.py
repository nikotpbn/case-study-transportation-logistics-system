from models.customer import Customer
from models.vehicle import Vehicle
from models.shipment import Shipment

customer_seed = [
    {
        "id": "ABC123",
        "name": "John Doe",
        "dob": "29/04/1989",
        "address": "123 Main St, Sydney, NSW 2000, Australia",
        "email": "john.doe@example.com",
        "phone_number": "0412345678",
    },
    {
        "id": "ABC234",
        "name": "Many Jane",
        "dob": "29/04/2005",
        "address": "234 Main St, Sydney, NSW 2000, Australia",
        "email": "mary.2005@test.net",
        "phone_number": "0487654321",
    },
]

vehicle_seed = [
    {
        "id": "V001",
        "type": "1",
        "capacity": "10000",
    },
    {
        "id": "V002",
        "type": "2",
        "capacity": "500",
    },
    {
        "id": "V003",
        "type": "3",
        "capacity": "200",
    },
]

shipment_seed = [
    {
        "id": "S001",
        "origin": "Sydney, NSW, Australia",
        "destination": "Melbourne, VIC, Australia)",
        "weight": 10,
        "vehicle": "V001",
    }
]


def seed():
    [Customer(**data).save() for data in customer_seed]
    [Vehicle(**data).save() for data in vehicle_seed]
    [Shipment(**data).save() for data in shipment_seed]
