"""Add admin config support

Revision ID: 1b5a90520562
Revises: 7f68eed434ab
Create Date: 2019-09-29 15:28:21.510635

"""

# revision identifiers, used by Alembic.
revision = '1b5a90520562'
down_revision = '7f68eed434ab'

from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

BaseTable = declarative_base()

class ConfigEntry(BaseTable):
    __tablename__ = 'config_entries'
    key = sa.Column(sa.String(255), primary_key=True)
    value = sa.Column(sa.Text(), nullable=False)
    public = sa.Column(sa.Boolean, default=False)

def upgrade():
    # Get alembic DB bind
    connection = op.get_bind()
    session = orm.Session(bind=connection)

    # Create new tables
    ConfigEntry.__table__.create(connection)
    # Seed default config values
    session.add(ConfigEntry(key='is_queue_open', value='true', public=True))
    session.add(ConfigEntry(key='welcome', value='Welcome to the OH queue!', public=True))

    session.commit()

def downgrade():
    # Get alembic DB bind
    connection = op.get_bind()

    # Create new tables
    op.drop_table('config_entries')
