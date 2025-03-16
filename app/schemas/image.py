from pydantic import BaseModel

class ImageBase(BaseModel):
    url: str

class ImageResponse(ImageBase):
    id: int

    class Config:
        from_attributes = True

class ImageCreate(ImageBase):
    pass
