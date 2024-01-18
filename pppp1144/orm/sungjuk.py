from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Sungjuk(Base):
    __tablename__='sungjuk'# 매핑할 테이블 지정
    sjno = Column(Integer, primary_key=True) # 오라클로 하려면 여기 바꿔야함
    name = Column(String(20)) #
    kor = Column(Integer)
    eng = Column(Integer)
    math = Column(Integer)
    tot = Column(Integer)
    avg = Column(Float)
    grd = Column(String(2))
    regdate = Column(DateTime, default=datetime.now(),
                     onupdate=datetime.now)

