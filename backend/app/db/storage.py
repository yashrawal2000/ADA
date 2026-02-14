from __future__ import annotations

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql+psycopg2://postgres:postgres@postgres:5432/trading")
engine = create_engine(POSTGRES_DSN, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
