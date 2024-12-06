"""add last few columns to post table

Revision ID: dc5da9d26fde
Revises: da3235f9bdf0
Create Date: 2024-12-04 22:20:47.620090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc5da9d26fde'
down_revision: Union[str, None] = 'da3235f9bdf0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
