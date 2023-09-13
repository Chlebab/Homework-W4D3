"""empty message

Revision ID: e52656d201c7
Revises: 
Create Date: 2023-09-13 13:27:54.390021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e52656d201c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clubs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('club_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('position', sa.String(length=64), nullable=True),
    sa.Column('club', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['club'], ['clubs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('players')
    op.drop_table('clubs')
    # ### end Alembic commands ###