"""empty message

Revision ID: 24656497c808
Revises: ffe0541a1c04
Create Date: 2018-05-12 11:09:07.536058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24656497c808'
down_revision = 'ffe0541a1c04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chapter', sa.Column('chapter_number', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chapter', 'chapter_number')
    # ### end Alembic commands ###
