# fastapi + pydantic + sqlalchemy를 조합한 예제

# main : zipcodev3
# orm : pppp1144.orm.Zipcode
# schema : pppp1144.model.ZipcodeRes
# dbengine : pppp1144.dbfactory
# dao : pppp1144.dato.ZipcodeDAO
#       select_zipcode,findbydong_zipcode

from typing import Optional
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI

app = FastAPI()


@app.get('/sungjuk',response_model=list[SungjukRes])
def getsungjuk():
    with Session()as sess:result = sess.query(Sungjuk).all()
    return result


@app.get('/sungjuk/{kor}',response_model=list[SungjukRes])
def getonesungjuk(kor):
    with Session()as sess:result = sess.query(Sungjuk).where(Sungjuk.dong.like(f'{kor}%')).all()
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sungjukv3:app", reload=True)