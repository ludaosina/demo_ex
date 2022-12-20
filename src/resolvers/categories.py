from sql_base.pharmacy_db import base_worker
from sql_base.models import Categories


def create_categories(categories: Categories):
    return base_worker.execute(query="INSERT INTO categories(name) VALUES (?) RETURNING id",
                               args=(categories.name,))


def get_categories(categories_id: int):
    return base_worker.execute(query="SELECT name FROM categories WHERE id = ?",
                               args=(categories_id,))


def update_categories(categories_id: int, new_data: Categories):
    return base_worker.execute(query="UPDATE categories SET name=? WHERE id=?",
                               args=(new_data.name, categories_id))


def delete_categories(categories_id: int):
    return base_worker.execute(query="DELETE FROM categories WHERE id=? ",
                               args=(categories_id,))
