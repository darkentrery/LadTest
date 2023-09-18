from datetime import datetime
import enum

from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship

from models.product import Product
from settings import Base


class PriceType(enum.Enum):
    retail = "retail"
    discount = "discount"
    bulk = "bulk"


class ProductPrice(Base):
    __tablename__ = "product_prices"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    price_type = Column(Enum(PriceType), default=PriceType.retail)
    url = Column(String, nullable=True)
    created = Column(TIMESTAMP, default=datetime.utcnow)
    update = Column(TIMESTAMP, default=datetime.utcnow)

    product_id = Column(Integer, ForeignKey(Product.id), primary_key=True)
    product = relationship("Product", foreign_keys='ProductPrice.product_id', back_populates="prices")
