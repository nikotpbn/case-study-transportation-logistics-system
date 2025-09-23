from colorama import Fore

from database import insert_customer, retrieve_customer, delete_customer, list_customers


class Customer:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.dob = kwargs.get("dob")
        self.address = kwargs.get("address")
        self.phone_number = kwargs.get("phone_number")
        self.email = kwargs.get("email")

    def save(self):
        insert_customer(self)

    def update(self, **kwargs):
        self.name = kwargs.get("name")
        self.dob = kwargs.get("dob")
        self.address = kwargs.get("address")
        self.phone_number = kwargs.get("phone_number")
        self.email = kwargs.get("email")
        print(Fore.GREEN + "Customer Information successfully updated")

    def delete(self):
        delete_customer(self.id)

    def to_list(self):
        [self.id, self.name, self.address, self.phone_number, self.email]

    @classmethod
    def all(cls):
        return list_customers()

    @classmethod
    def exists(cls, id):
        retrieve_customer()
