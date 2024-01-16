from fastapi import FastAPI
from models.schema import BookOneResp, BooksResp
from typing import Optional
from collections import OrderedDict
from models.schema import BookCreate
from pppp1144.BookDAO import BookDAO
from pppp1144.Book import Book


app = FastAPI()


@app.post('/book')
def newbook(bk: BookCreate):
    bk = bk.model_dump()

    bk = Book(bk['bkname'],bk['author'],bk['publisher'],
              bk['pubdate'],bk['retail'],bk['pctoff'])

    bk.price = int(bk.retail) * (1-int(bk.pctoff/100))
    bk.mileage = int(bk.retail) * int(bk.pctoff/100)

    rowcnt = BookDAO.insert_book(bk)
    result = f'{rowcnt} 건의 데이터가 수정되었습니다.'

    return result


#
# response_model을 지정한 탓에
# 조회 결과는 반드시 BooksResp 타입의 Json 형식이어야함
@app.get('/books',response_model=list[BooksResp])
def getbooks():
    rows = BookDAO.select_book()
    result = []
    for row in rows:
        data = OrderedDict()
        data['bkno'] = row[0]
        data['bkname'] = row[1]
        data['author'] = row[2]
        data['publisher'] = row[3]
        data['price'] = row[4]
        result.append(data)

    return result

@app.get('/book/{bkname}',response_model=Optional[BookOneResp])
def getonebook(bkname:str):
    result = None
    row = BookDAO.selectone_book(bkname)
    if row:
        result = OrderedDict()
        result['bkno'] = row[0]
        result['bkname'] = row[1]
        result['author'] = row[2]
        result['publisher'] = row[3]
        result['pubdate'] = row[4]
        result['retail'] = row[5]
        result['price'] = row[6]
        result['pctoff'] = row[7]
        result['mileage'] = row[8]
        result['regdate'] = row[9]

    return result


@app.put('/book')
def modifybooks(bk:BookCreate):
    bk = bk.model_dump()
    result = '데이터가 없어요!'
    row = BookDAO.selectone_book(bk['bkname'])

    if row:
        bk = Book(bk['bkname'],bk['author'],bk['publisher'],
                  bk['pubdate'],bk['retail'],bk['pctoff'])
        bk.bkno = int(row[0])
        bk.price = int(bk.retail) * (1-int(bk.pctoff/100))
        bk.mileage = int(bk.retail) * int(bk.pctoff/100)
        rowcnt = BookDAO.update_book(bk)
        result = f'{rowcnt} 건의 데이터가 수정되었습니다.'
    return result

@app.delete('/book/{bkno}')
def removebooks(bkno:int):
    rowcnt = BookDAO.delete_book(bkno)
    result = f'{rowcnt} 건의 데이터가 삭제되었습니다.'

    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("bookv1:app", reload=True)
