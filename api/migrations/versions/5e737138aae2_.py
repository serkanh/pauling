"""empty message

Revision ID: 5e737138aae2
Revises: b26756ac7225
Create Date: 2017-08-08 16:53:04.953458

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5e737138aae2'
down_revision = 'b26756ac7225'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posters', sa.Column('id_admin', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_unique_constraint(None, 'posters', ['id_admin'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posters', type_='unique')
    op.drop_column('posters', 'id_admin')
    # ### end Alembic commands ###