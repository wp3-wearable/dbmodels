from sqlalchemy import Column, Integer, String

from . import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(15), unique=True)
    address = Column(String(100))

    def __repr__(self):
        return '<User (id={}, name={})>'.format(self.id, self.name)
