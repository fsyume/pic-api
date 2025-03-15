from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.crud.image import get_images, create_image
from app.schemas.image import ImageCreate, ImageResponse

router = APIRouter()

# 依赖项：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/images", response_model=list[ImageResponse])
def read_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    images = get_images(db, skip=skip, limit=limit)
    return images

@router.post("/images", response_model=ImageResponse)
def add_image(image: ImageCreate, db: Session = Depends(get_db)):
    return create_image(db, image.url)
