from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel

class BookRes(BaseModel):
    bkno: Optional[int] = None
    bkname: str
    author: str
    publisher: str
    pubdate: datetime
    retail: int
    price: Optional[int] = None
    pctoff: int
    mileage : Optional[int] = None
    regdate : Union[None, datetime] = datetime.now()


    class Config:
        from_attributes = True