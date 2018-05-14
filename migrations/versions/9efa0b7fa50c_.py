"""empty message

Revision ID: 9efa0b7fa50c
Revises: 7427fcfea059
Create Date: 2018-05-12 09:56:24.748890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9efa0b7fa50c'
down_revision = '7427fcfea059'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('title', sa.Column('description', sa.String(length=2048), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('title', 'description')
    # ### end Alembic commands ###