"""Database configuration and session setup."""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///products.db")

# Create engine
engine = create_engine(
    DATABASE_URL, echo=False, future=True  # Set to True for SQL debugging
)

# Create session factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# Base class for models
Base = declarative_base()


def get_db():
    """Get database session."""
    return SessionLocal()


def init_db():
    """Initialize database tables."""
    Base.metadata.create_all(bind=engine)
