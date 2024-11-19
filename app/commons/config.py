# função : cria a conexão com o banco de dados e permite realizar operações no próprio
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def session_factory():
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOSTNAME = os.getenv('DB_HOSTNAME')
    DB_DATABASE = os.getenv('DB_DATABASE')

    engine = create_engine(f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_DATABASE}")
    _SessionFactory = sessionmaker(bind=engine)
    
    Base.metadata.create_all(engine, checkfirst=True)
    return _SessionFactory()