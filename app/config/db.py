from sqlalchemy import create_engine,column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

conn_string = "sqlite:///test.db"
engine = create_engine(conn_string)
Base = declarative_base()
Sessionlocal = sessionmaker(bind=engine)
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
Base.metadata.create_all(engine)
