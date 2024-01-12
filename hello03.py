# path parameter로 호출하기
# restful api 호출방식과 유사

# 여러 클라이언트로 테스트
# requests 이용
# import requests
# res = requests.get('http://127.0.0.1:8000/hi/python')
# res.text

# 2. httpx - 비동기 호출 가능
# import httpx
# res = httpx.get('http://127.0.0.1:8000/hi/python')
# res.text

# 3. httpie - 파이썬 도구, 요청/응답 상황 출력
# http 127.0.0.1:8000/hi    (서버 응답/본문 출력)
# http -b 127.0.0.1:8000/hi (헤더 생략)
# http -v 127.0.0.1:8000/hi (클라이언트/서버 헤더 본문 출력)




from fastapi import FastAPI

app = FastAPI()


@app.get("/hi/{msg}")
def greet(msg):
    from datetime import datetime
    result = f'{datetime.now()}'
    result = f'Hello,{msg}!!\n' + result
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello03:app", reload=True)
