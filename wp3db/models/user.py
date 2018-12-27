from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(15), unique=True)
    address = Column(String(100))

    def __repr__(self):
        return '<User (id={}, name={})>'.format(self.id, self.name)
