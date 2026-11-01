"""create posts table

Revision ID: 536e072c3c1f
Revises: 
Create Date: 2026-11-01 13:28:55.110386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '536e072c3c1f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable = False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
