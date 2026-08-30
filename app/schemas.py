from pydantic import BaseModel, HttpUrl


class ResourceCreate(BaseModel):
    url: HttpUrl


class ResourceResponse(BaseModel):
    id: int
    url: str
    title: str | None = None
    summary: str | None = None
    tags: str | None = None

    class Config:
        from_attributes = True