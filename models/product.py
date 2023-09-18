from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP

from settings import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    created = Column(TIMESTAMP, default=datetime.utcnow)
    update = Column(TIMESTAMP, default=datetime.utcnow)
