"""create dumpuser table

Revision ID: 8d903d809575
Revises: 
Create Date: 2023-10-14 23:27:59.195841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d903d809575'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dumpuser",
        sa.Column("userId", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("phone", sa.String(length=18), nullable=True),
        sa.Column("isActivate", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("userId"),
    )
    op.create_index(
        op.f("ix_dumpuser_userId"),
        "dumpuser",
        ["userId"],
        unique=False,
    )
    op.create_index(
        op.f("ix_dumpuser_phone"),
        "dumpuser",
        ["phone"],
        unique=False,
    )
    # pass


def downgrade() -> None:
    op.drop_index(
        op.f("ix_dumpuser_userId"),
        table_name="dumpuser",
    )
    op.drop_index(
        op.f("ix_dumpuser_phone"),
        table_name="dumpuser"
    )
    op.drop_table("dumpuser")
    # pass
