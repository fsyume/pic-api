from pydantic import BaseModel

class ImageBase(BaseModel):
    url: str

class ImageResponse(ImageBase):
    id: int

    class Config:
        orm_mode = True

class ImageCreate(ImageBase):
    pass
