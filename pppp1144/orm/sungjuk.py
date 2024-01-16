from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Sungjuk(Base):
    __tablename__='SUNGJUKS'# 매핑할 테이블 지정
    SJNO = Column(Integer(500))
    NAME = Column(String(30)) #
    KOR = Column(Integer(50))
    ENG = Column(Integer(50))
    MATH = Column(Integer(50))
    TOT = Column(Integer(100))
    AVG = Column(Integer(100))
    GRD = Column(String(100))
    REGDATE = None