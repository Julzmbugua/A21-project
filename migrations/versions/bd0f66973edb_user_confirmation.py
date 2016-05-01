"""user confirmation

Revision ID: bd0f66973edb
Revises: a25cd16f610c
Create Date: 2016-05-01 13:53:02.487456

"""

# revision identifiers, used by Alembic.
revision = 'bd0f66973edb'
down_revision = 'a25cd16f610c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###