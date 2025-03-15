from sqlalchemy.orm import Session
from app.models.image import Image


def get_images(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Image).offset(skip).limit(limit).all()


def create_image(db: Session, url: str):
    db_image = Image(url=url)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
