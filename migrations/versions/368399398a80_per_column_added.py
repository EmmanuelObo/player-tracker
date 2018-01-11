"""per column added

Revision ID: 368399398a80
Revises: bf7b326e31cc
Create Date: 2018-01-10 20:47:19.904441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '368399398a80'
down_revision = 'bf7b326e31cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('playerprofile', 'position')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('playerprofile', sa.Column('position', sa.VARCHAR(length=3), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
