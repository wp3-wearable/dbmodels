from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

# Specify database connection
engine = create_engine('sqlite:///wp3users.db')

# Create all the tables from models that subclassed Base
Base.metadata.create_all(engine)

# Create a Session class for external interfacing (see __init__.py)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
