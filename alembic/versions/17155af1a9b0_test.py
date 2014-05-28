"""test

Revision ID: 17155af1a9b0
Revises: None
Create Date: 2014-05-27 20:30:37.280000

"""

# revision identifiers, used by Alembic.
revision = '17155af1a9b0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_index('ix_users_nickname', 'users', ['nickname'], unique=True)
    op.drop_table('shots')
    op.alter_column('box', 'gameid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('game', 'away_team',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('game', 'date',
               existing_type=sa.DATETIME(),
               nullable=True)
    op.alter_column('game', 'home_outcome',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('game', 'home_team',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('pbp', 'away_score',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pbp', 'diff_score',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pbp', 'gameid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pbp', 'home_score',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pbp', 'stat_type',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('pbp', 'time',
               existing_type=sa.FLOAT(),
               nullable=True)
    op.alter_column('players', 'first_name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('players', 'height',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('players', 'last_name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('players', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('players', 'pclass',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('players', 'position',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('players', 'teamid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('team', 'teamid')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('teamid', sa.INTEGER(), nullable=True))
    op.alter_column('players', 'teamid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('players', 'position',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('players', 'pclass',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('players', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('players', 'last_name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('players', 'height',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('players', 'first_name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('pbp', 'time',
               existing_type=sa.FLOAT(),
               nullable=False)
    op.alter_column('pbp', 'stat_type',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('pbp', 'home_score',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pbp', 'gameid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pbp', 'diff_score',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pbp', 'away_score',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('game', 'home_team',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('game', 'home_outcome',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('game', 'date',
               existing_type=sa.DATETIME(),
               nullable=False)
    op.alter_column('game', 'away_team',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('box', 'gameid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_table('shots',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('gameid', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('first_name', sa.TEXT(), nullable=False),
    sa.Column('last_name', sa.TEXT(), nullable=False),
    sa.Column('x', sa.INTEGER(), nullable=False),
    sa.Column('y', sa.INTEGER(), nullable=False),
    sa.Column('time', sa.TEXT(), nullable=False),
    sa.Column('period', sa.INTEGER(), nullable=False),
    sa.Column('result', sa.INTEGER(), nullable=False),
    sa.Column('distance', sa.INTEGER(), nullable=False),
    sa.Column('team', sa.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['gameid'], [u'game.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_users_nickname', table_name='users')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
    ### end Alembic commands ###