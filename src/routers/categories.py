import fastapi
from sql_base.models import Categories
from resolvers.categories import create_categories, get_categories, get_all_categories, update_categories, delete_categories

categories_router = fastapi.APIRouter(prefix="/categories", tags=["Categories"])


@categories_router.get("/")
def start_page():
    return ""


@categories_router.post("/create/")
def new_categories(categories: Categories):
    return create_categories(categories)


@categories_router.get("/get/{categories_id}")
def search_categories(categories_id: int):
    return get_categories(categories_id)


@categories_router.get("/get/")
def search_all_categories():
    return get_all_categories()


@categories_router.put("/update/")
def upd_categories(categories_id: int, new_data: Categories):
    return update_categories(categories_id, new_data)


@categories_router.delete("/delete/")
def del_categories(categories_id: int):
    return delete_categories(categories_id)