import fastapi
from sql_base.models import Medicines
from resolvers.medicines import create_medicines, get_medicines, delete_medicines, update_medicines, get_all_medicines

medicines_router = fastapi.APIRouter(prefix="/medicines", tags=["Medicines"])


@medicines_router.get("/")
def start_page():
    return ""


@medicines_router.post("/create/")
def new_medicines(medicines: Medicines):
    return create_medicines(medicines)


@medicines_router.get("/get/{medicines_id}")
def search_medicines(medicines_id: int):
    return get_medicines(medicines_id)


@medicines_router.get("/get/")
def search_all_medicines():
    return get_all_medicines()


@medicines_router.put("/update/")
def upd_medicines(medicines_id: int, new_data: Medicines):
    return update_medicines(medicines_id, new_data)


@medicines_router.delete("/delete/")
def del_medicines(medicines_id: int):
    return delete_medicines(medicines_id)
