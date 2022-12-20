from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int]


class Pharmacy(BaseModelModify):
    address: str
    phone: int

