import sqlite3
from colorama import Fore

con = sqlite3.connect("tls.db")
cur = con.cursor()

"""Create tables if they do not exist"""


def create_tables():
    res = cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='fleet'"
    )
    if len(res.fetchall()) == 0:
        cur.execute("CREATE TABLE fleet(id, type, capacity)")

    res = cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='shipment'"
    )
    if len(res.fetchall()) == 0:
        cur.execute(
            "CREATE TABLE shipment(id, origin, destination, weight, vehicle, status)"
        )
    res = cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='delivery'"
    )
    if len(res.fetchall()) == 0:
        cur.execute(
            "CREATE TABLE delivery(shipment, datetime)"
        )


"""
Vehicles CRUD operations
"""


def retrieve_vehicle(vehicle_id):
    cur.execute("SELECT * FROM fleet WHERE id = ?", (vehicle_id,))
    vehicle = cur.fetchone()

    return vehicle if vehicle else False


def insert_vehicle(data):
    cur.execute(
        "INSERT INTO fleet (id, type, capacity) VALUES (?, ?, ?)",
        (data["id"], data["type"], data["capacity"]),
    )
    con.commit()
    print(Fore.GREEN + "Vehicle added successfully.")


def update_vehicle(data):
    cur.execute(
        "UPDATE fleet SET type = ?, capacity = ? WHERE id = ?",
        (data["type"], data["capacity"], data["id"]),
    )
    con.commit()
    print(Fore.GREEN + "Vehicle updated successfully.")


def delete_vehicle(vehicle_id):
    cur.execute("DELETE FROM fleet WHERE id = ?", (vehicle_id,))
    con.commit()
    print(Fore.GREEN + "Vehicle removed successfully.")


def list_vehicles():
    cur.execute("SELECT * FROM fleet")
    return cur.fetchall()


"""
Shipments CRUD operations
"""


def retrieve_shipment(shipment_id):
    cur.execute("SELECT * FROM shipment WHERE id = ?", (shipment_id,))
    shipment = cur.fetchone()

    return shipment if shipment else False


def insert_shipment(data):
    cur.execute(
        "INSERT INTO shipment (id, origin, destination, weight, vehicle, status) VALUES (?, ?, ?, ?, ?, ?)",
        (
            data["id"],
            data["origin"],
            data["destination"],
            data["weight"],
            data["vehicle"],
            data["status"],
        ),
    )
    con.commit()
    print(Fore.GREEN + "Shipment created successfully.")


def mark_shipment_delivered(shipment_id):
    cur.execute(
        "UPDATE shipment SET status = 'Delivered' WHERE id = ?",
        (shipment_id,),
    )
    con.commit()


def list_shipments():
    cur.execute("SELECT * FROM shipment")
    return cur.fetchall()

"""
Delivery CRUD operations
"""

def retrieve_delivery(shipment_id):
    cur.execute("SELECT * FROM delivery WHERE shipment = ?", (shipment_id,))
    delivery = cur.fetchone()

    return delivery if delivery else False

def insert_delivery(data):
    cur.execute(
        "INSERT INTO delivery (shipment, datetime) VALUES (?, ?)",
        (
            data["shipment"],
            data["datetime"],
        ),
    )
    con.commit()
    print(Fore.GREEN + "Delivery recorded successfully.")

def retrieve_delivery(shipment_id):
    cur.execute("SELECT * FROM delivery WHERE shipment = ?", (shipment_id,))
    delivery = cur.fetchone()

    return delivery if delivery else False