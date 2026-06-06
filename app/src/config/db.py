from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_size=10,          
    max_overflow=20,       
    pool_recycle=3600,     
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@contextmanager
def get_db_session():
    """Контекстный менеджер для безопасной работы с БД."""
    session = SessionLocal()
    try:
        yield session
        session.commit()  
    except Exception:
        session.rollback() 
        raise
    finally:
        session.close()    