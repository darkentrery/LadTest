from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from models.product_category import ProductCategory
from models.product_price import ProductPrice
from models.product_info import ProductInfo
from models.city import City
from settings import Base


class ProductInfoLink(Base):
    __tablename__ = 'product_info_links'

    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    product_info_id = Column(Integer, ForeignKey('product_info.id'), primary_key=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    created = Column(TIMESTAMP, default=datetime.utcnow)
    updated = Column(TIMESTAMP, default=datetime.utcnow)

    product_category_id = Column(Integer, ForeignKey(ProductCategory.id), primary_key=True)
    product_category = relationship("ProductCategory", foreign_keys='Product.product_category_id', back_populates="products")
    prices = relationship("ProductPrice", back_populates="product")
    product_infos = relationship("ProductInfoLink", backref="product")
    product_cities = relationship("CityProductLink", backref="product")
