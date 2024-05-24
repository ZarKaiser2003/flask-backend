from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from settings import get_env_variable
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine(f"postgresql://postgres:postgres@localhost:5432/{get_env_variable('POSTGRES_DB')}")

Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    from app.modules.sys.sys import SysUsers
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
