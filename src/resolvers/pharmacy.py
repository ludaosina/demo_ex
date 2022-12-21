from sql_base.pharmacy_db import base_worker
from sql_base.models import Pharmacy


def create_pharmacy(pharmacy: Pharmacy):
    return base_worker.execute(query="INSERT INTO pharmacy(address, phone) VALUES (?, ?) RETURNING id",
                               args=(pharmacy.address, pharmacy.phone))


def get_pharmacy(pharmacy_id: int):
    return base_worker.execute(query="SELECT address, phone FROM pharmacy WHERE id = ?",
                               args=(pharmacy_id,))


def get_all_pharmacy():
    return base_worker.execute(query="SELECT id, address, phone FROM pharmacy",
                               many=True)


def update_pharmacy(pharmacy_id: int, new_data: Pharmacy):
    return base_worker.execute(query="UPDATE pharmacy SET address=?, phone=? WHERE id=?",
                               args=(new_data.address, new_data.phone, pharmacy_id))


def delete_pharmacy(pharmacy_id: int):
    return base_worker.execute(query="DELETE FROM pharmacy WHERE id=? ",
                               args=(pharmacy_id,))
