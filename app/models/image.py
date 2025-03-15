from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
