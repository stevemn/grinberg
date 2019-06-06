"""empty message

Revision ID: 4400bbd8efc7
Revises: 6d4d80b8d2b3
Create Date: 2019-06-06 09:32:36.777204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4400bbd8efc7'
down_revision = '6d4d80b8d2b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
