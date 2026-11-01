"""add other cols to posts

Revision ID: 746e6124e036
Revises: 95f0832f29f0
Create Date: 2026-11-01 15:05:52.509268

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '746e6124e036'
down_revision: Union[str, None] = '95f0832f29f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable = False ,server_default = "True"))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable = False , server_default = sa.text('Now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','created_at')
    op.drop_column('posts','published')
    pass
