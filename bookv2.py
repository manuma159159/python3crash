from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greet(msg):

    return {greet}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("bookv1:app", reload=True)
