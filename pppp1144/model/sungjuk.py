from datetime import datetime
from typing import Optional
from pydantic import BaseModel



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



