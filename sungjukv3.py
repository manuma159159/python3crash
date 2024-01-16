# fastapi + pydantic + sqlalchemy를 조합한 예제
# main : zipcodev3
# orm : pppp1144.orm.Zipcode
# schema : pppp1144.model.ZipcodeRes
# dbengine : pppp1144.dbfactory
# dao : pppp1144.dato.ZipcodeDAO
#       select_zipcode,findbydong_zipcode

from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI
from pppp1144.SungJukService import SungJukService
from sqlalchemy import insert,update,delete
from models.schema import SungjuksResponse

app = FastAPI()


ousr =''
opwd =''
ourl = ''
#sqlalchemy 설정
database_url = ''
#database_url = f'oracle+cx_oracle://{ousr}:{opwd}@{ourl}'
engine = create_engine(database_url,echo=True)
Session = sessionmaker(autocommit=False, autoflush=False,bind=engine)

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
    # now()가 아닌 now인 이유는 지속적인 업데이트시에도 시간을
    # 변경하기 위함이디ㅏ.


class SungjukRes(BaseModel):
    sjno: Optional[int] = None # insert시 시스템이 대신 입력해주도록 None으로 설정
    name: str
    kor: int
    eng: int
    math: int
    tot: Optional[int] = 0
    avg: Optional[float] = 0.0
    grd: Optional[str] = '가'
    regdate : Optional[datetime] = None

    class Config:
        from_attribute = True # 2.0 verison
        #orm_mode = 1.4 version

Base.metadata.create_all(engine)

# 성적 데이터 조회 - 번호,이름,국어,영어,수학, 등록일
@app.get("/sungjuk",response_model=list[SungjukRes])
def getsungjuk():
    with Session()as sess:
        result = sess.query(Sungjuk).offset(0).limit(10).all()
    return result

# 성적 데이터 검색
@app.get("/sungjuk/{sjno}",response_model=SungjukRes)
def getonesungjuk(sjno:int):

    with Session()as sess:
        #result = sess.query(Sungjuk).where(Sungjuk.sjno==sjno).first()
        result = sess.query(Sungjuk).filter_by(sjno=sjno).first()
    return result
    # 이거는 세션 닫기 close를 자동으로 실해해주는 코드

# 성적데이터 등록
@app.post("/sungjuk", response_model=str)
def newsungjuk(sj:SungjukRes):
    data = sj.model_dump()
    sj = Sungjuk(**data)
    SungJukService.compute_sungjuk(sj)
    data = {'name': sj.name, 'kor': sj.kor, 'eng': sj.eng, 'math': sj.math,
            'tot': sj.tot, 'avg': sj.tot, 'grd': sj.grd}

    with Session() as sess:
    #     sess.add(sj)
    #     sess.commit()
    #
    # result = (f'1건의 성적데이터 추가됨!!')
    # return = result
        stmt = insert(Sungjuk).values(data)
        result = sess.execute(stmt)
        sess.commit()
    return f'{result.rowcount}건의 데이터가 추가됨'

# 성적데이터 수정
@app.put("/sungjuk/{sjno}")
def modifysungjuk(sj:SungjukRes):
    data = sj.model_dump()
    sj=Sungjuk(**data)
    SungJukService.compute_sungjuk(sj)
    data={'kor':sj.kor,'eng':sj.eng,'math':sj.math,
          'tot':sj.tot,'avg':sj.tot,'grd':sj.grd}
    with Session() as sess:
    #     sess.query(Sungjuk).filter_by(sjno=sj.sjno).update(data)
    #     sess.commit()
    #result=(f'1건의 정보가 수정되었습니다.')
    #return result
        stmt = update(Sungjuk).values(data).filter_by(sjno=sj.sjno)
        result = sess.execute(stmt)
        sess.commit()
    return f'{result.rowcount}건의 성적데이터 수정됨!'

@app.delete("/sungjuk/{sjno}")
def remove(sjno):
    with Session() as sess:
    #     sess.query(Sungjuk).filter_by(sjno=sjno).delete()
    #     sess.commit()
    # result = f'1건의 데이터가 삭제되었습니다.'
    # return result
        stmt = delete(Sungjuk).filter_by(sjno=sjno)
        result = sess.execute(stmt)
        sess.commit()
    return f'{result.rowcount} 건의 정보가 삭제됨'



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sungjukv3:app", reload=True)


























