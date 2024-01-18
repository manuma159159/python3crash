from typing import Optional
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI

app = FastAPI()

#sqlalchemy 설정
database_url = ''
engine = create_engine(database_url,echo=True)
Session = sessionmaker(autocommit=False, autoflush=False,bind=engine)


# orm 객체설정
Base = declarative_base()
class Zipcode(Base):
    __tablename__='zipcode2013'# 매핑할 테이블 지정
    zipcode = Column(String(7))
    sido = Column(String(7))
    gugun = Column(String(50))
    dong = Column(String(50))
    ri = Column(String(50))
    bunji = Column(String(100))
    seq = Column(Integer,Sequence('zipseq'), primary_key=True)

# 직렬화 객체 설정

class ZipcodeRes(BaseModel):
    zipcode : str
    sido : str
    gugun : str
    dong : str
    ri : Optional[str] = ''# 해당 컬럼의 값이 null이면 공백으로 출력
    bunji : Optional[str] = ''
    seq : int

    class config:
        orm_mode = True


# 우편번호 데이터 전체 조회
@app.get("/zipcode",response_model=list[ZipcodeRes])
def getzipcode():

    # sess = Session()
    # result = sess.query(Zipcode).offset(0).limit(20).all()
    #
    # sess.close()
    with Session()as sess:result = sess.query(Zipcode).offset(0).limit(20).all()
    return result


# 우편번호 데이터 검색
@app.get("/zipcode/{dong}",response_model=list[ZipcodeRes])
def findzipcode(dong):
    # sess = Session()
    # result = sess.query(Zipcode).where(Zipcode.dong.like(f'{dong}%')).all()
    #
    # sess.close()
    with Session()as sess:result = sess.query(Zipcode).where(Zipcode.dong.like(f'{dong}%')).all()
    return result
    # 이거는 세션 닫기 close를 자동으로 실해해주는 코드




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("zipcodev2b:app", reload=True)