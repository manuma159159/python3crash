# pydantic
# 데이터의 유효성 검사 및 직렬화/역직렬화 지원도구
# pip install pydantic

# 영화정보를 pydantic으로 정의
# 영화번호, 영화명, 장르, 평점, 태그, 상영일자, 기타정보

from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List
from datetime import datetime


class Movie(BaseModel):
    mvno: int     # 정수형
    mvname: str   # 문자형
    genre: List[str]    # 여러개의 문자로 구성된 리스트
    rate: Union[int,float]  #정수나 실수 중 하나
    mvdate: Optional[datetime]    # 날짜시간 (필수는 x) 옵셔널: 있어도 없어도 ok
    audien: int = 0     # 정수인데 기본값이 0 이건 관객수
    reserve: Union[int,float]   # 예약수


# 객체 생성
movie = {'mvno':1, 'mvname':'외계+인2', 'genre':['SF','멜로','공포'], 'rate':3.2,
         'mvdate':'2024-01-10 12:12:12', 'audien':168407, 'reserve':40.5}
# 만약에 mvno쪽에 aa라는 문자를 넣으면 바로 문제생김

try:
    mv1 = Movie(**movie)
except ValidationError as e:
    print('입력오류') # 이거는 입력값 다른거 넣엏을 때 일단 오류라고 하는거.




# 클래스2 정의 : constraint type 사용 - deprecated 예정 ( 곧 사라질 기능 )
from pydantic import constr,conlist,conint, PositiveInt,BaseModel, Field # 포지티브 = 양수

class Movie2(BaseModel):
    userid: constr(min_length=6, max_length=15)    # 글자수 최소 6 최대 15
    genre: conlist(str,min_length=2, max_length=5) # 장르 항목 수 최소2 최대5
    rate: conint(ge=1, le=5)
    audien: PositiveInt     # 누적관객수는 양수

movie = { 'userid':'abc1234', 'rate':3, 'audien': 1000, 'genre': ['SF','멜로','공포'] }

Movie2(**movie)

from models.schema import Sungjuk
from models.schema import SungjukBase
from models.schema import SungjukResponse
sj =  {"name":"abc123", "kor":99, "eng":98, "math":99}
Sungjuk(**sj)
SungjukBase(**sj)

sj= {"name":"abc123", "kor":99, "eng":98, "math":99, 'sjno':1, 'tot': 297,
     'avg':99.9, 'grd': '수', 'regdate': '2020-01-12 12:12:12'}

SungjukResponse(**sj)


# 클래스3 정의 :  Field 사용
from pydantic import Field

class Movie3(BaseModel):
    userid: str = Field(min_length=6, max_length=15)    # 글자수 최소 6 최대 15
    genre: list[str] = Field(min_length=2, max_length=5) # 장르 항목 수 최소2 최대5
    rate: int = Field(ge=1, le=5)
    audien: PositiveInt     # 누적관객수는 양수