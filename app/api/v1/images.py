from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.crud.image import get_images, create_image, get_image_by_id, update_image, delete_image
from app.schemas.image import ImageCreate, ImageResponse, ImageUpdate

router = APIRouter()


# 依赖项：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 获取所有图片
@router.get("/images", response_model=list[ImageResponse])
def read_images(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    images = get_images(db, skip=skip, limit=limit)
    return images


# 获取单个图片
@router.get("/images/{image_id}", response_model=ImageResponse)
def read_image(image_id: int, db: Session = Depends(get_db)):
    image = get_image_by_id(db, image_id)
    if not image:
        raise HTTPException(status_code=404, detail="图片未找到")
    return image


# 添加图片
@router.post("/images", response_model=ImageResponse)
def add_image(image: ImageCreate, db: Session = Depends(get_db)):
    return create_image(db, image.url)


# 更新图片链接
@router.put("/images/{image_id}", response_model=ImageResponse)
def modify_image(image_id: int, image_update: ImageUpdate, db: Session = Depends(get_db)):
    updated_image = update_image(db, image_id, image_update.url)
    if not updated_image:
        raise HTTPException(status_code=404, detail="图片未找到")
    return updated_image


# 删除图片
@router.delete("/images/{image_id}")
def remove_image(image_id: int, db: Session = Depends(get_db)):
    success = delete_image(db, image_id)
    if not success:
        raise HTTPException(status_code=404, detail="图片未找到")
    return {"message": "图片删除成功"}
