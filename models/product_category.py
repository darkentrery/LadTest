from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from settings import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    products = relationship("Product", back_populates="product_category")
