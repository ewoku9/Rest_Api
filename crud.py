from sqlalchemy.orm import Session
from db_models import Item
from schemas import ItemCreate

# создание предмета 
def create_item(db: Session, item: ItemCreate):
    db_item = Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# get предмета 
def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()
