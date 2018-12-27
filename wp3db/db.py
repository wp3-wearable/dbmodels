import sqlalchemy
from sqlalchemy.orm import sessionmaker

from .models import Base

engine = sqlalchemy.create_engine('sqlite:///wp3users.db')

Base.metadata.create_all(engine)
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
