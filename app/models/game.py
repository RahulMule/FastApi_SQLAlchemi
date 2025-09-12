from app.config.db import Base
from sqlalchemy import Integer,String,Column
from sqlalchemy.orm import declarative_base

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)



