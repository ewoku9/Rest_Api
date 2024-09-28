from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db_models import Base, Item 
from database import SessionLocal, engine 
from schemas import ItemCreate, Item as ItemSchema  
from crud import create_item, get_items 
from typing import List

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=ItemSchema)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

@app.get("/items/", response_model=List[ItemSchema])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = get_items(db=db, skip=skip, limit=limit)
    return items
