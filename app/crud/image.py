from sqlalchemy.orm import Session
from app.models.image import Image


# 获取所有图片
def get_images(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Image).offset(skip).limit(limit).all()

# 创建图片链接
def create_image(db: Session, url: str):
    db_image = Image(url=url)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

# 根据 ID 获取单个图片
def get_image_by_id(db: Session, image_id: int):
    return db.query(Image).filter(Image.id == image_id).first()

# 更新图片链接
def update_image(db: Session, image_id: int, new_url: str):
    db_image = db.query(Image).filter(Image.id == image_id).first()
    if db_image:
        db_image.url = new_url
        db.commit()
        db.refresh(db_image)
    return db_image

# 删除图片
def delete_image(db: Session, image_id: int):
    db_image = db.query(Image).filter(Image.id == image_id).first()
    if db_image:
        db.delete(db_image)
        db.commit()
        return True
    return False