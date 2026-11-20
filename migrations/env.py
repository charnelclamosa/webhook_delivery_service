import os

from alembic import context
from sqlalchemy import create_engine, pool


def run_migrations_online() -> None:
  """Apply migrations using the configured PostgreSQL connection."""
  engine = create_engine(os.environ["DATABASE_URL"], poolclass=pool.NullPool)

  try:
    with engine.connect() as connection:
      context.configure(connection=connection)

      with context.begin_transaction():
        context.run_migrations()
  finally:
    engine.dispose()


run_migrations_online()