from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def app_info():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    return {"message": "submit csv"}
