from pydantic import BaseModel


# 基础模型
class ImageBase(BaseModel):
    url: str


# 返回数据格式
class ImageResponse(ImageBase):
    id: int

    class Config:
        from_attributes = True


# 创建图片数据格式
class ImageCreate(ImageBase):
    pass


# 更新图片数据格式
class ImageUpdate(BaseModel):
    url: str
