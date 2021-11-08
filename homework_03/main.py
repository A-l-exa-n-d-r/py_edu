from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world!!!"}


@app.get("/ping/", status_code=200)
async def ping():
    return {"message": "pong"}
