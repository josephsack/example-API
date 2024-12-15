"""auto-vote

Revision ID: b45ea434e02f
Revises: dc5da9d26fde
Create Date: 2024-12-04 22:31:47.474378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b45ea434e02f'
down_revision: Union[str, None] = 'da3235f9bdf0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.alter_column('posts', 'published',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('posts', 'created_at',
               existing_type=postgresql.TIME(timezone=True),
               type_=sa.TIMESTAMP(timezone=True),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'created_at',
               existing_type=sa.TIMESTAMP(timezone=True),
               type_=postgresql.TIME(timezone=True),
               nullable=True)
    op.alter_column('posts', 'published',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_table('votes')
    # ### end Alembic commands ###
