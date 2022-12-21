import fastapi
from sql_base.models import Supplier
from resolvers.supplier import create_supplier, get_supplier, delete_supplier, update_supplier, get_all_supplier

supplier_router = fastapi.APIRouter(prefix="/supplier", tags=["Supplier"])


@supplier_router.get("/")
def start_page():
    return ""


@supplier_router.post("/create/")
def new_supplier(supplier: Supplier):
    return create_supplier(supplier)


@supplier_router.get("/get/{client_id}")
def search_supplier(supplier_id: int):
    return get_supplier(supplier_id)


@supplier_router.get("/get/")
def search_all_supplier():
    return get_all_supplier()


@supplier_router.put("/update/")
def upd_supplier(supplier_id: int, new_data: Supplier):
    return update_supplier(supplier_id, new_data)


@supplier_router.delete("/delete/")
def del_supplier(supplier_id: int):
    return delete_supplier(supplier_id)
