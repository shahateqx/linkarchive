from fastapi import FastAPI

from app.database import create_tables
from app.routes.resources import router as resources_router

app = FastAPI(title="LinkArchive")


@app.on_event("startup")
def startup():
    create_tables()


@app.get("/")
def root():
    return {"message": "LinkArchive API is running"}


app.include_router(resources_router)