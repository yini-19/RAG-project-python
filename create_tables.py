from db import engine
from models import Base
from sqlalchemy import inspect

Base.metadata.create_all(engine)
print("Tables created successfully.")

inspector = inspect(engine)
print("Tables now visible to this engine:", inspector.get_table_names())