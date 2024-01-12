
import sqlite3


from fastapi import FastAPI

app = FastAPI()

# 기본페이지
@app.get("/")
def index():
    # 응답은 언제나 json으로
    return {'msg':'Hello,World'}

# 우편번호 데이터 전체 조회
@app.get("/zipcode")
def getzipcode():
    conn = sqlite3.connect('bigdata.db')
    cursor = conn.cursor()
    sql = 'select * from zipcode2013 limit 0,100'
    cursor.execute(sql)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    result = ''
    for row in rows:
        result += f'{row[0],row[1],row[2],row[3]}'
    # 응답은 언제나 json으로
    return f'{result}'


# 우편번호 데이터 검색
@app.get("/zipcode/{dong}")
def findzipcode(dong):

    conn = sqlite3.connect('bigdata.db')
    cursor = conn.cursor()
    sql = 'select * from zipcode2013 where dong like ?'
    params = [dong + '%']
    cursor.execute(sql,params)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()


    result = ''
    for row in rows:

        result = f'{row[0]}{row[1]}{row[2]}{row[3]}{row[4]}{row[5]}'

    return f'{result}'



    # 응답은 언제나 json으로
    return {}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("zipcodev1:app", reload=True)
