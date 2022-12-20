from sql_base.pharmacy_db import base_worker
from sql_base.models import Client


def create_client(client: Client):
    return base_worker.execute(query="INSERT INTO client(name, phone) VALUES (?, ?) RETURNING id",
                               args=(client.name, client.phone))


def get_client(client_id: int):
    return base_worker.execute(query="SELECT name, phone FROM client WHERE id = ?",
                               args=(client_id,))


def update_client(client_id: int, new_data: Client):
    return base_worker.execute(query="UPDATE client SET name=?, phone=? WHERE id=?",
                               args=(new_data.name, new_data.phone, client_id))


def delete_client(client_id: int):
    return base_worker.execute(query="DELETE FROM client WHERE id=? ",
                               args=(client_id,))
