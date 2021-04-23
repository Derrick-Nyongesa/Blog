"""posts

Revision ID: ab8001068338
Revises: 3af0a03bfa12
Create Date: 2021-04-23 18:30:08.980432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab8001068338'
down_revision = '3af0a03bfa12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('pitch', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
