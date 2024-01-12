# 쿼리문자열 querystring으로 호출 가능
# 즉, ? 뒤에 오는 키 = 값 문자열로 특정 api 호출
# 레거시(옛날) api 호출 방식



# 여러 클라이언트로 테스트 (이거는 파이썬 콘솔로 실행)
# requests 이용
# import requests
# res = requests.get('http://127.0.0.1:8000/hi?msg=python')
# res.text

# params = {"msg":"python"}
# res = requests.get('http://127.0.0.1:8000/hi', params=params)
# res.text



# 2. httpx - 비동기 호출 가능
# import httpx
# res = httpx.get('http://127.0.0.1:8000/hi/python')
# res.text

# 3. httpie - 파이썬 도구, 요청/응답 상황 출력
# http 127.0.0.1:8000/hi?msg=python    (서버 응답/본문 출력)
# http -b 127.0.0.1:8000/hi?msg=python (헤더 생략)
# http -v 127.0.0.1:8000/hi?msg=python (클라이언트/서버 헤더 본문 출력)
# http -v 127.0.0.1:8000/hi msg==python (클라이언트/서버 헤더 본문 출력) 위에거랑 똑같다

#path parameter는 쿼리문자열 querystring로도 호출 가능


from fastapi import FastAPI

app = FastAPI()


@app.get("/hi")
def greet(msg):
    from datetime import datetime
    result = f'{datetime.now()}'
    result = f'Hello,{msg}!!\n' + result
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello04:app", reload=True)
