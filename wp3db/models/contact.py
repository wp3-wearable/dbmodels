from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class Contact(Base):
    __tablename__ = 'contacts'

    name = Column(String(50))
    phone = Column(String(15))
    address = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='contacts')

    def __repr__(self):
        return '<Contact (name={}, phone={})>'.format(
                self.name, self.phone
        )
