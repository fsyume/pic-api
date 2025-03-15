from fastapi import FastAPI
from app.api.v1 import images
from app.core.database import Base, engine

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 路由
app.include_router(images.router, prefix="/api/v1", tags=["Images"])
