"""convert to timescale db

Revision ID: c36e8ea624c7
Revises: 8d903d809575
Create Date: 2024-04-06 06:05:48.973581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c36e8ea624c7'
down_revision: Union[str, None] = '8d903d809575'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Get the table information from the database
    conn = op.get_bind()
    existing_metadata = sa.schema.MetaData()
    table_name = 'dumpuser'
    time_col = 'time_created'
    setup_hypertable= f"SELECT create_hypertable('{table_name}', '{time_col}',migrate_data => true);"
    existing_table = sa.Table(table_name, existing_metadata, autoload_with=conn)
    # Operate to update table
    op.add_column(table_name, 
                  sa.Column(time_col, sa.DateTime)
    )
    op.drop_constraint(existing_table.primary_key.name,table_name)
    op.create_primary_key(time_col,table_name,[time_col])
    op.execute(f"{setup_hypertable}")
def downgrade() -> None:
    table_name='dumpuser'
    time_col = 'time_created'
    op.drop_constraint(time_col, table_name, type_='primary')
    op.create_primary_key('userId', table_name, ['userId'])

    # Drop the new column
    op.drop_column(table_name, time_col)
