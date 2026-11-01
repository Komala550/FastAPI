"""add phonenum to user

Revision ID: 24daf80187b7
Revises: d1a54901d4de
Create Date: 2026-11-01 15:19:02.381401

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24daf80187b7'
down_revision: Union[str, None] = 'd1a54901d4de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
