"""new fields in user table

Revision ID: 0f15d3e3a661
Revises: 2625d3551679
Create Date: 2020-06-16 20:20:26.864009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f15d3e3a661'
down_revision = '2625d3551679'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
