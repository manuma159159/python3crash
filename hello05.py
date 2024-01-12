# 요청 본문으로 호출 가능
# 즉, 새로운 데이터를 생성하거나 수정할 때 종종 사용
# 단, 요청 본문은 json 형식이어야함.

# 자동화 된 문서
# http://127.0.0.1:8000/docs - fastapi의 앤드포인트(path) 테스트 페이지


# 여러 클라이언트로 테스트 (이거는 파이썬 콘솔로 실행)
# 1. requests 이용
# import json
# data = {"msg":"python"}
# res = requests.post('http://127.0.0.1:8000/hi', data=json.dumps(data))
# res.text



# 2. httpx - 비동기 호출 가능
# import httpx
# res = httpx.get('http://127.0.0.1:8000/hi/python')
# res.text

# 3. httpie - 파이썬 도구, 요청/응답 상황 출력
# http 127.0.0.1:8000/hi msg=python    (서버 응답/본문 출력)
# http -b 127.0.0.1:8000/hi msg=python (헤더 생략)
# http -v 127.0.0.1:8000/hi msg=python (클라이언트/서버 헤더 본문 출력)
# http -v 127.0.0.1:8000/hi msg=python (클라이언트/서버 헤더 본문 출력) 위에거랑 똑같다

#path parameter는 쿼리문자열 querystring로도 호출 가능


from fastapi import FastAPI, Body

app = FastAPI()


@app.post("/hi")
def greet(msg=Body(embed=True)):
    from datetime import datetime
    result = f'{datetime.now()}'
    result = f'Hello,{msg}!!\n' + result
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello04:app", reload=True)
