"""add content column to post tableaddUserTable

Revision ID: 06ea068c9af0
Revises: 926d45a05388
Create Date: 2026-11-01 14:55:26.650804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06ea068c9af0'
down_revision: Union[str, None] = '926d45a05388'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text('now()')
        )
    )


def downgrade() -> None:
    op.drop_table('users')
