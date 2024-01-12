from fastapi import FastAPI
from pppp1144.BookDAO import BookDAO
from pppp1144.Book import Book

app = FastAPI()


@app.post("/book")
def newsungjuk(msg):

    return {greet}

@app.get()
def getsungjuk(msg):

    return {greet}

@app.get()
def getonesungjuk(msg):

    return {greet}

@app.put()
def modifysungjuk(msg):

    return {greet}

@app.delete()
def remove(msg):

    return {greet}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("bookv1:app", reload=True)
