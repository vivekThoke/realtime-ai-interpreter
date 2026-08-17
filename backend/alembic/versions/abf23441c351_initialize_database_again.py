"""Initialize Database again

Revision ID: abf23441c351
Revises: d172302b588c
Create Date: 2026-08-17 19:31:30.149500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abf23441c351'
down_revision: Union[str, Sequence[str], None] = 'd172302b588c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
