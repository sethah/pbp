"""initial

Revision ID: 4d638425e5a4
Revises: None
Create Date: 2014-05-28 18:23:27.827000

"""

# revision identifiers, used by Alembic.
revision = '4d638425e5a4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###

    op.drop_column('team', 'teamid')
    op.add_column('users', sa.Column('name', sa.String(length=64), nullable=True))
    op.create_index('ix_users_name', 'users', ['name'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_name', table_name='users')
    op.drop_column('users', 'name')
    op.add_column('team', sa.Column('teamid', sa.INTEGER(), nullable=True))
    
    ### end Alembic commands ###
