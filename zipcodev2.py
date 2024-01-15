
from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base

from fastapi import FastAPI

app = FastAPI()

#sqlalchemy 설정
database_url = 'sqlite:///bigdata.db'
engine = create_engine(database_url,echo=True)
Session = sessionmaker(bind=engine)


# orm 객체설정
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


# 우편번호 데이터 전체 조회
@app.get("/zipcode")
def getzipcode():

    sess = Session()
    rows = sess.query(Zipcode).offset(0).limit(20).all()

    result = ''
    for row in rows:
        result += f'{row.zipcode}{row.sido}{row.gugun}{row.dong}'

    sess.close()
    # 응답은 언제나 json으로
    return f'{result}'


# 우편번호 데이터 검색
@app.get("/zipcode/{dong}")
def findzipcode(dong):
    sess = Session()
    rows = sess.query(Zipcode).where(Zipcode.dong.like(f'{dong}%')).all()

    result = ''
    for row in rows:

        result = f'{row.zipcode}{row.sido}{row.gugun}{row.dong}'
    sess.close()
    return f'{result}'



    # 응답은 언제나 json으로
    return {}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("zipcodev2:app", reload=True)
