from collections import OrderedDict

from pppp1144.SungJuk import Sungjuk
from pppp1144.SungJukService import SungJukService
from pppp1144.SungJukDAO import SungJukDAO
import sys

from fastapi import FastAPI
from models.schema import SungjukResponse,SungjukBase,SungjuksResponse
app = FastAPI()


# 성적데이터 등록
# 성적데이터는 요청 본문에 담아 서버로 전송
# "sj": {"name":"abc123", "kor":99, "eng":98, "math":99}
# type hint를 이용해서 데이터 추가시 추가되는 데이터의 타입을 강제할 수 있음
# 또한, response_model을 이용해서 응답 메세지의 타입도 강제할 수 있음
@app.post("/sungjuk", response_model=str)
def newsungjuk(sj:SungjukBase):
    # sj = SungjukBase(**dict(sj)) #json으로 넘어온 데이터를 dict로 바꿈
    # return sj

    #sj = dict(sj)
    sj = sj.model_dump()    # pydandic의 model_dump도 가능
    sj = Sungjuk(sj['name'],sj['kor'],sj['eng'],sj['math'])
    SungJukService.compute_sungjuk(sj)
    rowcnt = SungJukDAO.insert_sungjuk(sj)
    result = (f'{rowcnt} 건의 성적데이터 추가됨!!')
    return result


# 성적 데이터 조회 - 번호,이름,국어,영어,수학, 등록일
@app.get("/sungjuk",response_model=list[SungjuksResponse]) # 기본적으로 / sungjuk 이거 다르게 써야하는데 post/get 처럼 다른 방식으로 열어서 ㄱㅊ음
def getsungjuk():
    rows = SungJukDAO.select_sungjuk() # 이거 마리아디비로 하는거라 DAO 들어가서 dbinfo 마리아디비로 바꿔야함

    result = []
    for row in rows:
        data = OrderedDict()
        data['sjno']=row[0]
        data['name']=row[1]
        data['kor']=row[2]
        data['eng']=row[3]
        data['math']=row[4]
        data['regdate']=str(row[5])[:10]

        result.append(data)


    return result


# 성적데이터 검색 = 번호로 조회
@app.get("/sungjuk/{sjno}",response_model=SungjukResponse)
def getonesungjuk(sj:int):
    result = {'sjno':-1 ,'name':'', 'kor':-1, 'eng':-1, 'math':-1, 'tot':-1,
              'avg':-1, 'grd':'', 'regdate': '0001-01-01 00:00:00'}
    row = SungJukDAO.selectone_sungjuk(sj['sjno'])

    if row:
        result = OrderedDict
        data = OrderedDict()
        data['sjno']=row[0]
        data['name']=row[1]
        data['kor']=row[2]
        data['eng']=row[3]
        data['math']=row[4]
        data['tot']=row[5]
        data['avg']=row[6]
        data['grd']=row[7]
        data['regdate']=row[8]


    return result


# 성적데이터 수정
@app.put("/sungjuk/{sjno}")
def modifysungjuk(sj:SungjukBase):

    result = '데이터가 없어요'
    row = SungJukDAO.selectone_sungjuk(sj['sjno'])

    if row:
        data = Sungjuk(sj['name'],sj['kor'],sj['eng'],sj['math'])
        SungJukService.compute_sungjuk(data)

        rowcnt = SungJukDAO.update_sungjuk(data,sj['sjno'])
        result = f'{rowcnt}의 데이터가 수정되었습니다.'

    return result


# 성적데이터 삭제
@app.delete("/sungjuk/{sjno}")
def remove(sjno):

    rowcnt = SungJukDAO.delete_sungjuk(sjno)
    result = f'{rowcnt}의 데이터가 삭제되었습니다.'
    # 응답은 언제나 json으로
    return result





if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sungjukv2:app", reload=True)
