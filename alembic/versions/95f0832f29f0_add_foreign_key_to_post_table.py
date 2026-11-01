"""add foreign key to post table

Revision ID: 95f0832f29f0
Revises: 06ea068c9af0
Create Date: 2026-11-01 15:00:02.079322

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95f0832f29f0'
down_revision: Union[str, None] = '06ea068c9af0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable = False))
    op.create_foreign_key('post_user_fk',source_table='posts',referent_table='users',local_cols = ['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass

