"""add ListURI table

Revision ID: fd25da4e8425
Revises: 13f66995fb32
Create Date: 2024-08-23 16:50:18.334938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd25da4e8425'
down_revision: Union[str, None] = '13f66995fb32'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('list_uri',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uri', sa.String(), nullable=False),
    sa.Column('list_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('list_uri')
    # ### end Alembic commands ###
