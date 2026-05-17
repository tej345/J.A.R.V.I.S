from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# the database address goes here
DATABASE_URL = "postgresql://postgres:Andromeds2111%40@127.0.0.1:5432/jarvis_db"

# the engine (physical connection pipe)
engine = create_engine(
    DATABASE_URL,
    connect_args={"host":"127.0.0.1"}
)

# the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# the base class
Base = declarative_base()

# the database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
