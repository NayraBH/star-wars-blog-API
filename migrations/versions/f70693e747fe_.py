"""empty message

Revision ID: f70693e747fe
Revises: 793b1fed9f0b
Create Date: 2022-04-24 09:37:59.213178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f70693e747fe'
down_revision = '793b1fed9f0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('birth_year', sa.Integer(), nullable=True))
    op.add_column('people', sa.Column('gender', sa.String(length=120), nullable=True))
    op.add_column('people', sa.Column('height', sa.String(length=120), nullable=True))
    op.add_column('people', sa.Column('skin_color', sa.String(length=120), nullable=True))
    op.add_column('people', sa.Column('eye_color', sa.String(length=120), nullable=True))
    op.add_column('planet', sa.Column('climate', sa.String(length=120), nullable=True))
    op.add_column('planet', sa.Column('population', sa.String(length=120), nullable=True))
    op.add_column('planet', sa.Column('orbital_period', sa.String(length=120), nullable=True))
    op.add_column('planet', sa.Column('rotation_period', sa.String(length=120), nullable=True))
    op.add_column('planet', sa.Column('diameter', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planet', 'diameter')
    op.drop_column('planet', 'rotation_period')
    op.drop_column('planet', 'orbital_period')
    op.drop_column('planet', 'population')
    op.drop_column('planet', 'climate')
    op.drop_column('people', 'eye_color')
    op.drop_column('people', 'skin_color')
    op.drop_column('people', 'height')
    op.drop_column('people', 'gender')
    op.drop_column('people', 'birth_year')
    # ### end Alembic commands ###
