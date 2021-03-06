"""adjustments

Revision ID: c2d73de82c2d
Revises: d5c29b2292ea
Create Date: 2018-01-09 18:57:04.850694

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c2d73de82c2d'
down_revision = 'd5c29b2292ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playerprofile')
    op.drop_table('users')
    op.drop_table('playerstats')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playerstats',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ppg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('rpg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('apg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('pie', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('bpg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('spg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='playerstats_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=130), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_table('playerprofile',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('height', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('weight', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('prior', sa.VARCHAR(length=15), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('experience', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('picture', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='playerprofile_pkey')
    )
    # ### end Alembic commands ###
