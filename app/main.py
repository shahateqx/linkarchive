from fastapi import FastAPI

app = FastAPI(title="LinkArchive")


@app.get("/")
def root():
    return {"message": "LinkArchive API is running"}