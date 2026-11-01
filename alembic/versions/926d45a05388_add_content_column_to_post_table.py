"""add content column to post table

Revision ID: 926d45a05388
Revises: 536e072c3c1f
Create Date: 2026-11-01 14:37:02.178914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '926d45a05388'
down_revision: Union[str, None] = '536e072c3c1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
