from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./filemeta.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class FileMeta(Base):
    __tablename__ = "file_meta"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    owner = Column(String)

def create_db():
    Base.metadata.create_all(bind=engine)
