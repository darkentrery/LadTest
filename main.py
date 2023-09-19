from sqlalchemy import select

from models.product import Product
from settings import session


def run():
    products = session.execute(select(Product)).scalars().all()
    pass


if __name__ == "__main__":
    run()
    