from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from settings import Base


class CityProductLink(Base):
    __tablename__ = 'city_product_links'

    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    city_id = Column(Integer, ForeignKey('cities.id'), primary_key=True)


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    city_products = relationship("CityProductLink", backref="city")
