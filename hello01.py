# FastAPI
# FastAPI는 현대적이고, 빠르며(고성능), 파이썬 표준 타입 힌트에 기초한
# Python3.8+의 API를 빌드하기 위한 웹 프레임워크입니다
# 비동기 처리를 위한 starlatte
# 모델 정의와 유효성 검사를 위한 pydantic
# 비동기 웹서버를 위한 uvicorn

# fastapi 앱 실행
# uvicorn 파일명:app --reload (uvicorn hello01:app --reload)


from fastapi import FastAPI

app=FastAPI()


@app.get("/hi")
def greet():
    from datetime import datetime
    msg = f'{datetime.now()}'
    msg = 'Hello,world!!\n' + msg
    return msg
