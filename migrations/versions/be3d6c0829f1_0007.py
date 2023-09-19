"""0007

Revision ID: be3d6c0829f1
Revises: 
Create Date: 2023-09-19 07:00:24.277010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be3d6c0829f1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_cities_id'), 'cities', ['id'], unique=False)
    op.create_table('product_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_product_categories_id'), 'product_categories', ['id'], unique=False)
    op.create_table('product_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_product_info_id'), 'product_info', ['id'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated', sa.TIMESTAMP(), nullable=True),
    sa.Column('product_category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_category_id'], ['product_categories.id'], ),
    sa.PrimaryKeyConstraint('id', 'product_category_id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=True)
    op.create_table('city_product_links',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'city_id')
    )
    op.create_table('product_info_links',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_info_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['product_info_id'], ['product_info.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'product_info_id')
    )
    op.create_table('product_prices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('price_type', sa.Enum('retail', 'discount', 'bulk', name='pricetype'), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('created', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated', sa.TIMESTAMP(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id', 'product_id')
    )
    op.create_index(op.f('ix_product_prices_id'), 'product_prices', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_prices_id'), table_name='product_prices')
    op.drop_table('product_prices')
    op.drop_table('product_info_links')
    op.drop_table('city_product_links')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_product_info_id'), table_name='product_info')
    op.drop_table('product_info')
    op.drop_index(op.f('ix_product_categories_id'), table_name='product_categories')
    op.drop_table('product_categories')
    op.drop_index(op.f('ix_cities_id'), table_name='cities')
    op.drop_table('cities')
    # ### end Alembic commands ###