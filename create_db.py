from database import engine
from models.item import Item

# Create all tables
Item.metadata.create_all(bind=engine)
