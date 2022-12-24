from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int]


class Pharmacy(BaseModelModify):
    address: str
    phone: int


class Supplier(BaseModelModify):
    address: str
    phone: int
    company_name: str


class Client(BaseModelModify):
    name: str
    phone: int


class Categories(BaseModelModify):
    name: str


class Medicines(BaseModelModify):
    category_id: int
    name: str
    price: int


class List(BaseModelModify):
    pharmacy_id: int
    medicines_id: int


class UserLogin(BaseModelModify):
    login: str
    password: str


class Users(UserLogin):
    power_level: int
