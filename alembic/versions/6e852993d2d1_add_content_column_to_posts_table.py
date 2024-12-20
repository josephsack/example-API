"""add content column to posts table

Revision ID: 6e852993d2d1
Revises: a4fc6ee1e566
Create Date: 2024-12-04 17:27:28.828820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e852993d2d1'
down_revision: Union[str, None] = 'a4fc6ee1e566'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
