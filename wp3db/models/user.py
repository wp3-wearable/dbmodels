from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base, Contact


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(15), unique=True)
    address = Column(String(100))

    contacts = relationship('Contact', order_by=Contact.id,
                            back_populates='user')

    def __repr__(self):
        return '<User (id={}, name={})>'.format(self.id, self.name)
