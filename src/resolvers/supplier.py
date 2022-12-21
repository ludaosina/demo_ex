from sql_base.pharmacy_db import base_worker
from sql_base.models import Supplier


def create_supplier(supplier: Supplier):
    return base_worker.execute(query="INSERT INTO supplier(address, phone, company_name) VALUES (?, ?, ?) RETURNING id",
                               args=(supplier.address, supplier.phone, supplier.company_name))


def get_all_supplier():
    return base_worker.execute(query="SELECT id, address, phone, company_name FROM supplier")


def get_supplier(supplier_id: int):
    return base_worker.execute(query="SELECT address, phone, company_name FROM supplier WHERE id =?",
                               args=(supplier_id,))


def update_supplier(supplier_id: int, new_data: Supplier):
    return base_worker.execute(query="UPDATE supplier SET address=?, phone=?, company_name=? WHERE id=?",
                               args=[new_data.address, new_data.phone, new_data.company_name, supplier_id])


def delete_supplier(supplier_id: int):
    return base_worker.execute(query="DELETE FROM supplier WHERE id=? ",
                               args=(supplier_id,))