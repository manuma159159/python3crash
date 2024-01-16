from typing import Union,Optional,List
from pydantic import BaseModel,ValidationError
from datetime import datetime, date


class Sungjuk(BaseModel):
    sjno: Optional[int] = None
    name: str
    kor: int
    eng: int
    math: int
    tot: Optional[int] = None
    avg: Optional[float] = None
    grd: Optional[str] = None
    regdate : Optional[datetime] = None




class SungjukBase(BaseModel):
    name: str
    kor: int
    eng: int
    math: int


class SungjuksResponse(SungjukBase):
    sjno:int
    regdate:date


class SungjukResponse(SungjuksResponse):
    tot: int
    avg: float
    grd: str
    regdate : datetime  # 이거 date은 날짜만 나오는데 datetime으로 덮어버리는거임.



class book(BaseModel):
    bkno: Optional[int] = None
    bkname: str
    author: str
    publlisher: int
    pubdate: datetime
    retail: str
    price: int
    pcroff: int
    mileage : int
    regdate : datetime

class BookCreate(BaseModel):
    bkname: str
    author: str
    publisher: int
    pubdate: datetime
    retail: int
    pctoff: int


# bkname, author, publisher,price
class BooksResp(BookCreate):
    bkno: int
    price: int
    pubdate: Optional[datetime] = datetime(1970,1,1)
    retail: Optional[int] = 0
    pctoff: Optional[int] = 0


class BookOneResp(BooksResp):
    mileage: int
    regdate: datetime