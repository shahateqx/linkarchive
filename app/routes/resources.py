from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import engine
from app.models import Resource
from app.schemas import ResourceCreate, ResourceResponse

router = APIRouter(prefix="/resources", tags=["resources"])


def get_db():
    with Session(engine) as session:
        yield session


@router.post("", response_model=ResourceResponse, status_code=201)
def create_resource(
    resource_data: ResourceCreate,
    db: Session = Depends(get_db),
):
    existing = (
        db.query(Resource)
        .filter(Resource.url == str(resource_data.url))
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Resource with this URL already exists",
        )

    resource = Resource(url=str(resource_data.url))

    db.add(resource)
    db.commit()
    db.refresh(resource)

    return resource

@router.get("", response_model=list[ResourceResponse])
def get_resources(db: Session = Depends(get_db)):
    return db.query(Resource).order_by(Resource.created_at.desc()).all()