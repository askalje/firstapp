from fastapi import Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal
from models.item import Item

app= FastAPI()
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        return {
            "id": item.id,
            "name": item.name,
            "price": item.price,
            "description": item.description
        }
    raise HTTPException(status_code=404, detail="Item not found")
