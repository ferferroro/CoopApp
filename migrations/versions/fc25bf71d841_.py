"""empty message

Revision ID: fc25bf71d841
Revises: 3fd2116b1781
Create Date: 2020-01-05 05:36:45.825993

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fc25bf71d841'
down_revision = '3fd2116b1781'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contribution',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('member_code', sa.String(length=20), nullable=True),
    sa.Column('period', sa.String(length=7), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('remarks', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contribution')
    # ### end Alembic commands ###