"""initialize database

Revision ID: d172302b588c
Revises:
Create Date: 2026-08-16 20:33:57.718131

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "d172302b588c"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
