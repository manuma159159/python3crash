from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, Sequence, Float, DateTime, text
from sqlalchemy.orm import sessionmaker, declarative_base
from pppp1144.SungJukService import SungJukService

# 데이터베이스 연결준비
database_url = ''
#database_url = '' # mariadb
#database_url = ''

engine = create_engine(database_url,echo=True)

# 데이터베이스 엔진을 이용해서 세션 생성
Session = sessionmaker(bind=engine)


# ORM 객체 생성을 위한 Base 클래스 선언
Base = declarative_base()


class Sungjuk(Base):
    __tablename__='sungjuk'# 매핑할 테이블 지정
    sjno = Column(Integer, autoincrement=True, primary_key=True)
    # sjseq = Sequence('sjseq',metadata = Base.metadata)
    # sjno = Column(Integer,sjseq,primary_key=True) 이거 두개는 오라클용 이거는 오라클 11 이하
    # sjno = Column(Integer,Identity(start=1,maxvalue=1000000 ,cache=None,cycle=None), primary_key=True) 오라클 12 이상
    name = Column(String(20)) #
    kor = Column(Integer)
    eng = Column(Integer)
    math = Column(Integer)
    tot = Column(Integer,default=0)
    avg = Column(Float,default=0)
    grd = Column(String(2),default='가')
    #regdate = Column(DateTime,default=text('current_timestamp' )) #utc 시간으로 잡힘. 세계 기본 시간
    regdate = Column(DateTime,default=datetime.now()) #utc 시간으로 잡힘. 세계 기본 시간


class SungjukRes(BaseModel):
    sjno: Optional[int] = None
    name: str
    kor: int
    eng: int
    math: int
    tot: Optional[int] = 0
    avg: Optional[float] = 0.0
    grd: Optional[str] = '가'
    regdate : Optional[datetime] = datetime(1970,1,1)

    class Config:
        from_attribute = True # 2.0 verison
        #orm_mode = 1.4 version

Base.metadata.create_all(engine)

#데이터 추가 - add
data = {'name':'abc1234','kor':99,'eng':98,'math':99}
sj = Sungjuk(**data)
SungJukService.compute_sungjuk(sj)

print(sj.name,sj.kor)

with Session()as sess:
    sess.add(sj)
    sess.commit()


# 데이터 수정 - update

sjno=1
data = {'name':'abc1234','kor':11,'eng':22,'math':33}
# data = Sungjuk(**data)
# SungJukService.compute_sungjuk(data)
data['regdate'] = datetime.now()

with Session()as sess:
    #sess.query(Sungjuk).where(Sungjuk.sjno==sjno).update(data)
    sess.query(Sungjuk).filter_by(sjno=sjno).update(data)
    sess.commit()


# 데이터 삭제 - delete
sjno=4
with Session()as sess:
    #sess.query(Sungjuk).where(Sungjuk.sjno==sjno).delete()
    sess.query(Sungjuk).filter_by(sjno=sjno).delete()
    sess.commit()

# 부분조회
with Session() as sess:
    result = sess.query(Sungjuk.sjno, Sungjuk.name, Sungjuk.kor, Sungjuk.eng, Sungjuk.math,
                        Sungjuk.regdate).all()
    print(result)