from database import engine
from models.items import Item

# Create all tables
Item.metadata.create_all(bind=engine)
