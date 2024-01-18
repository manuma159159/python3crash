from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, func

from pppp1144.dbfactory import engine

Base = declarative_base()

class Book(Base):
    __tablename__='book'
    bkno = Column(Integer, primary_key=True, autoincrement=True)
    bkname = Column(String(50))
    author = Column(String(50))
    publisher = Column(String(50))
    pubdate = Column(DateTime)
    retail = Column(Integer)
    price = Column(Integer, server_default='0')
    pctoff = Column(Integer)
    mileage = Column(Integer, server_default='0')
    # regdate = Column(DateTime, default=datetime.now(),
    #                            onupdate=datetime.now)
    regdate = Column(DateTime, server_default=func.now(),
                     onupdate=datetime.now)

Base.metadata.create_all(engine)