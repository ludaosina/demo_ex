import fastapi
from server.sql_base.models import Users
from server.resolvers.users import create_users, get_users, delete_users, update_users, get_all_users

users_router = fastapi.APIRouter(prefix="/users ", tags=["Users "])


@users_router.get("/")
def start_page():
    return ""


@users_router.post("/create/")
def new_users(users: Users):
    return create_users(users)


@users_router.get("/get/{users_id}")
def search_users(users_id: int):
    return get_users(users_id)


@users_router.get("/get/")
def search_all_users():
    return get_all_users()


@users_router.put("/update/{users_id}")
def upd_users(users_id: int, new_data: Users):
    return update_users(users_id, new_data)


@users_router.delete("/delete/{users_id}")
def del_users(users_id: int):
    return delete_users(users_id)
