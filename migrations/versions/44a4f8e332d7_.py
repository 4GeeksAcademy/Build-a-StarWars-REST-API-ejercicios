"""empty message

Revision ID: 44a4f8e332d7
Revises: 6663007610da
Create Date: 2023-07-10 22:25:41.079101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44a4f8e332d7'
down_revision = '6663007610da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###