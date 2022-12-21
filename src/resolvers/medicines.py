from sql_base.pharmacy_db import base_worker
from sql_base.models import Medicines


def create_medicines(medicines: Medicines):
    return base_worker.execute(query="INSERT INTO medicines(category_id, name, price) VALUES (?, ?, ?) RETURNING id",
                               args=(medicines.category_id, medicines.name, medicines.price))


def get_medicines(medicines_id: int):
    return base_worker.execute(query="SELECT id, category_id, name, price FROM medicines WHERE id = ?",
                               args=(medicines_id,))


def get_all_medicines():
    return base_worker.execute(query="SELECT id, category_id, name, price FROM medicines",
                               many=True)


def update_medicines(medicines_id: int, new_data: Medicines):
    return base_worker.execute(query="UPDATE medicines SET category_id=?, name=?, price=? WHERE id=?",
                               args=(new_data.category_id, new_data.name, new_data.price, medicines_id))


def delete_medicines(medicines_id: int):
    return base_worker.execute(query="DELETE FROM medicines WHERE id=? ",
                               args=(medicines_id,))
