"""
Description of the model for the database of two entities: a book, an author.
"""

from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from db_setup.db_connect import EngineDB

Base = declarative_base()


class Brand(Base):
    """ Brand essence """
    __tablename__ = 'brand'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


engine = EngineDB().connect_db()
Base.metadata.create_all(engine)
