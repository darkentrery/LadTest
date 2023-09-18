from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from models.product_category import ProductCategory
from settings import Base


class ProductInfoLink(Base):
    __tablename__ = 'product_info_links'

    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    product_info_id = Column(Integer, ForeignKey('product_info.id'), primary_key=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    created = Column(TIMESTAMP, default=datetime.utcnow)
    update = Column(TIMESTAMP, default=datetime.utcnow)

    product_category_id = Column(Integer, ForeignKey(ProductCategory.id), primary_key=True)
    product_category = relationship("ProductCategory", foreign_keys='Product.product_category_id', back_populates="products")
    prices = relationship("ProductPrice", back_populates="product_price")
    product_infos = relationship("ProductInfo", secondary='product_info_links')
    product_cities = relationship("City", secondary='city_product_links')
