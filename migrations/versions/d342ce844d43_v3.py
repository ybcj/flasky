"""v3

Revision ID: d342ce844d43
Revises: fd8e4ef1a12f
Create Date: 2018-10-02 14:49:08.544300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd342ce844d43'
down_revision = 'fd8e4ef1a12f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
