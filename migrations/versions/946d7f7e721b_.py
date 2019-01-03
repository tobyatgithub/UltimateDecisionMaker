"""empty message

Revision ID: 946d7f7e721b
Revises: 9258d8127a4f
Create Date: 2019-01-02 14:20:15.217390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '946d7f7e721b'
down_revision = '9258d8127a4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('decisions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('decision', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('decisions')
    # ### end Alembic commands ###