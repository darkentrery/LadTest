from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from settings import Base


class ProductInfo(Base):
    __tablename__ = "product_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    value = Column(Float)

    products = relationship("ProductInfoLink", backref='product_info')

    @property
    def k(self):
        return "f"
