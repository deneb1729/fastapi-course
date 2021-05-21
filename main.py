from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "hello human"


@app.get("/about")
def index():
    return {"data": ["about page"]}



