"""add foreign-key to posts table

Revision ID: da3235f9bdf0
Revises: f9e3683f90fc
Create Date: 2024-12-04 21:50:32.496158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da3235f9bdf0'
down_revision: Union[str, None] = 'f9e3683f90fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
