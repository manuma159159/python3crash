from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, String, Integer, Sequence

Base = declarative_base()
class Zipcode(Base):
    __tablename__='zipcode2013'# 매핑할 테이블 지정
    zipcode = Column(String(7)) # zipcode가 일곱글자라 7이 오는거임
    sido = Column(String(7)) #
    gugun = Column(String(50))
    dong = Column(String(50))
    ri = Column(String(50))
    bunji = Column(String(100))
    seq = Column(Integer,Sequence('zipseq'), primary_key=True)