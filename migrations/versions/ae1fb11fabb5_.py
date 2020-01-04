"""empty message

Revision ID: ae1fb11fabb5
Revises: 1291cb958a84
Create Date: 2020-01-05 02:17:22.134946

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ae1fb11fabb5'
down_revision = '1291cb958a84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sequence',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('prefix', sa.String(length=10), nullable=True),
    sa.Column('increment', sa.Integer(), nullable=True),
    sa.Column('current', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sequence')
    # ### end Alembic commands ###
