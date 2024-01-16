
from typing import Optional

from pydantic import BaseModel



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