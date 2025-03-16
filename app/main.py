import uvicorn
from fastapi import FastAPI
from app.api.v1 import images, jump301
from app.core.database import Base, engine

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 路由
app.include_router(jump301.router)
app.include_router(images.router, prefix="/api/v1", tags=["Images"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
