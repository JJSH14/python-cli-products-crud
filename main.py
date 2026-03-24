"""Main entry point for the application."""

from cli import cli
from database import init_db

if __name__ == "__main__":
    # Ensure database is initialized on first run
    try:
        init_db()
    except Exception:
        pass

    cli()
