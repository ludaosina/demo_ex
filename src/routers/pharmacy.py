import fastapi
from sql_base.models import Pharmacy
from resolvers.pharmacy import create_pharmacy, get_pharmacy, delete_pharmacy, update_pharmacy, get_all_pharmacy

pharmacy_router = fastapi.APIRouter(prefix="/pharmacy", tags=["Pharmacy"])


@pharmacy_router.get("/")
def start_page():
    return ""


@pharmacy_router.post("/create/")
def new_client(pharmacy: Pharmacy):
    return create_pharmacy(pharmacy)


@pharmacy_router.get("/get/{pharmacy_id}")
def search_pharmacy(pharmacy_id: int):
    return get_pharmacy(pharmacy_id)


@pharmacy_router.get("/get/")
def search_all_pharmacy():
    return get_all_pharmacy()


@pharmacy_router.put("/update/")
def upd_pharmacy(pharmacy_id: int, new_data: Pharmacy):
    return update_pharmacy(pharmacy_id, new_data)


@pharmacy_router.delete("/delete/")
def del_pharmacy(pharmacy_id: int):
    return delete_pharmacy(pharmacy_id)
