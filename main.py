from sqlalchemy import desc

from models.product import Product
from models.product_price import ProductPrice
from settings import session


def run():
    query = session.query(ProductPrice, Product).join(ProductPrice, Product.id == ProductPrice.product_id).order_by(desc(ProductPrice.updated))
    found_records = query.cte()
    prices = session.query(found_records).distinct(found_records.c.product_id).all()
    for price in prices:
        print(price)


if __name__ == "__main__":
    run()
    