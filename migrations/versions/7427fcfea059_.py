"""empty message

Revision ID: 7427fcfea059
Revises: 01d1bcbd1994
Create Date: 2018-05-11 11:58:24.355561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7427fcfea059'
down_revision = '01d1bcbd1994'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chapter', sa.Column('read_url', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chapter', 'read_url')
    # ### end Alembic commands ###
