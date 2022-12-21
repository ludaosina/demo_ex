import fastapi
from sql_base.models import List
from resolvers.list import create_list, get_list, delete_list, update_list, get_all_list

list_router = fastapi.APIRouter(prefix="/list", tags=["List"])


@list_router.get("/")
def start_page():
    return ""


@list_router.post("/create/")
def new_list(list: List):
    return create_list(list)


@list_router.get("/get/{list_id}")
def search_list(list_id: int):
    return get_list(list_id)


@list_router.get("/get/")
def search_all_list():
    return get_all_list()


@list_router.put("/update/")
def upd_list(list_id: int, new_data: List):
    return update_list(list_id, new_data)


@list_router.delete("/delete/")
def del_list(list_id: int):
    return delete_list(list_id)
