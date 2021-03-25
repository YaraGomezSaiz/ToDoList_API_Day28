"""empty message

Revision ID: 4780d9aefed3
Revises: 7ccbcf77d746
Create Date: 2021-03-25 18:25:30.264476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4780d9aefed3'
down_revision = '7ccbcf77d746'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('is_done', sa.Boolean(), nullable=False))
    op.drop_index('id', table_name='todos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('id', 'todos', ['id'], unique=True)
    op.drop_column('todos', 'is_done')
    # ### end Alembic commands ###
