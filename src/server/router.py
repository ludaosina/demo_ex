from server.routers.pharmacy import pharmacy_router
from server.routers.list import list_router
from server.routers.users import users_router
from server.routers.client import client_router
from server.routers.supplier import supplier_router
from server.routers.categories import categories_router
from server.routers.medicines import medicines_router

routers = (pharmacy_router, list_router, users_router, client_router, supplier_router, categories_router, medicines_router)