"""add phonenum to user

Revision ID: 0fad7d99c467
Revises: 24daf80187b7
Create Date: 2026-11-01 15:21:20.596574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fad7d99c467'
down_revision: Union[str, None] = '24daf80187b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
