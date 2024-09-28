from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# схема Item
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# создание Item
class ItemCreate(ItemBase):
    pass

# отображение item
class Item(ItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True 