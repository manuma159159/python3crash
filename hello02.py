# python 코드로 fastapi 앱 실행
# if __name__ == "__main__": 라는 문장 사용

# 여러 클라이언트로 테스트
# requests 이용
# import requests
# res = requests.get('http://127.0.0.1:8000/hi')
# res.text

# 2. httpx - 비동기 호출 가능
# import httpx
# res = httpx.get('http://127.0.0.1:8000/hi')
# res.text

# 3. httpie - 파이썬 도구, 요청/응답 상황 출력
# http 127.0.0.1:8000/hi    (서버 응답/본문 출력)
# http -b 127.0.0.1:8000/hi (헤더 생략)
# http -v 127.0.0.1:8000/hi (클라이언트/서버 헤더 본문 출력)



from fastapi import FastAPI

app = FastAPI()


@app.get("/hi")
def greet():
    from datetime import datetime
    msg = f'{datetime.now()}'
    msg = 'Hello,world!!\n' + msg
    return msg


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello02:app", reload=True)
