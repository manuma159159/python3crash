from pppp1144.SungJuk import Sungjuk
from pppp1144.SungJukService import SungJukService
from pppp1144.SungJukDAO import SungJukDAO
import sys

from fastapi import FastAPI, Body

app = FastAPI()


# 성적데이터 등록
# "sj": {"name":"abc123", "kor":99, "eng":98, "math":99}  fastapi에 execute 할 때
# 성적데이터는 요청 본문에 담아 서버로 전송
@app.post("/sungjuk")
def newsungjuk(sj=Body(embed=True)):
    sj = Sungjuk(sj['name'],sj['kor'],sj['eng'],sj['math']) #json 방식으로 나가야하기 때문에 [] 쓴 것.
    SungJukService.compute_sungjuk(sj)

    rowcnt = SungJukDAO.insert_sungjuk(sj)
    result = (f'{rowcnt} 건의 성적데이터 추가됨!!')
    return result


# 성적 데이터 조회 - 번호,이름,국어,영어,수학, 등록일
@app.get("/sungjuk") # 기본적으로 / sungjuk 이거 다르게 써야하는데 post/get 처럼 다른 방식으로 열어서 ㄱㅊ음
def getsungjuk():
    rows = SungJukDAO.select_sungjuk() # 이거 마리아디비로 하는거라 DAO 들어가서 dbinfo 마리아디비로 바꿔야함

    result = ''
    for row in rows:
        result += (f'{row[0]},{row[1]},{row[2]},{row[3]},'
                   f'{row[4]},{str(row[5])[:10]}')


    return f'{result}'


# 성적데이터 검색 = 번호로 조회
@app.get("/sungjuk/{sjno}")
def getonesungjuk(sj):
    result = '데이터 없어요'
    row = SungJukDAO.selectone_sungjuk(sj['sjno'])

    if row:
        result +=(f' {row[0]} {row[1]} {row[2]} {row[3]} {row[4]} '
                  f' {row[5]} {row[6]} {row[7]} {row[8]} ')
    return result


# 성적데이터 수정
@app.put("/sungjuk/{sjno}")
def modifysungjuk(sj=Body(embed=True)):

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
    uvicorn.run("sungjukv1:app", reload=True)
