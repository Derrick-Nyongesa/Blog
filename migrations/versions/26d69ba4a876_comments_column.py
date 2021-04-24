"""comments column

Revision ID: 26d69ba4a876
Revises: 9867bd43bee7
Create Date: 2021-04-24 09:12:40.074408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26d69ba4a876'
down_revision = '9867bd43bee7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'posted')
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###