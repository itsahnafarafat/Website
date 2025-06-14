"""Add Job and User models

Revision ID: ab5b171ce485
Revises: 
Create Date: 2025-05-21 05:38:41.805423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab5b171ce485'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('job')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), nullable=False),
    sa.Column('company', sa.VARCHAR(length=100), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('location', sa.VARCHAR(length=100), nullable=False),
    sa.Column('posted_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=150), nullable=False),
    sa.Column('password', sa.VARCHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###
