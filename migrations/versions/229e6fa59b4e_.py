"""empty message

Revision ID: 229e6fa59b4e
Revises: 
Create Date: 2022-03-16 12:53:25.922798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '229e6fa59b4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pessoas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.Column('sexo', sa.String(length=1), nullable=True),
    sa.Column('salario', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pessoas')
    # ### end Alembic commands ###
