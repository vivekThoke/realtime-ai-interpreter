"""Initialize Database again

Revision ID: abf23441c351
Revises: d172302b588c
Create Date: 2026-08-17 19:31:30.149500

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "abf23441c351"
down_revision: str | Sequence[str] | None = "d172302b588c"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
