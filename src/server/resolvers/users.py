from server.sql_base.pharmacy_db import base_worker
from server.sql_base.models import Users, UserLogin


def create_users(user: Users):
    return base_worker.execute(query="INSERT INTO users(login, password, power_level) VALUES (?, ?, ?) RETURNING id",
                               args=(user.login, user.password, user.power_level))


def get_users(users_id: int):
    return base_worker.execute(query="SELECT id, login, password, power_level FROM users WHERE id = ?",
                               args=(users_id,))


def get_all_users():
    return base_worker.execute(query="SELECT id, login, password, power_level FROM users",
                               many=True)


def update_users(users_id: int, new_data: Users):
    return base_worker.execute(query="UPDATE users SET (login, password, power_level) = (?, ?, ?) WHERE id=?",
                               args=(new_data.login, new_data.password, new_data.power_level, users_id))


def delete_users(users_id: int):
    return base_worker.execute(query="DELETE FROM users WHERE id=? ",
                               args=(users_id,))


def check_login(login: UserLogin):
    return base_worker.execute(query="SELECT power_level FROM users WHERE (login, password) = (?, ?)",
                               args=(login.login, login.password))
