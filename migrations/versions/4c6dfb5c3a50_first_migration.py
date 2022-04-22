"""First Migration

Revision ID: 4c6dfb5c3a50
Revises: 
Create Date: 2022-04-22 16:31:26.430367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c6dfb5c3a50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('make', sa.String(length=255), nullable=True),
    sa.Column('model', sa.String(length=255), nullable=True),
    sa.Column('colour', sa.String(length=255), nullable=True),
    sa.Column('year', sa.String(length=255), nullable=True),
    sa.Column('transmission', sa.String(length=255), nullable=True),
    sa.Column('car_type', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=1024), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('fullname', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('biography', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('date_joined', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    op.drop_table('Favourites')
    op.drop_table('Cars')
    # ### end Alembic commands ###
