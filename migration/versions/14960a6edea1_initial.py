"""initial

Revision ID: 14960a6edea1
Revises: 
Create Date: 2022-09-09 09:27:26.261795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14960a6edea1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('game', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.create_unique_constraint(None, 'game', ['name'])
    op.alter_column('user', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.TEXT(),
               nullable=True)
    op.create_unique_constraint(None, 'user', ['email'])
    op.create_unique_constraint(None, 'user', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'email',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('user', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.drop_constraint(None, 'game', type_='unique')
    op.alter_column('game', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###
