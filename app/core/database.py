import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 确保 data 目录存在
os.makedirs("data", exist_ok=True)

# 读取 .env 中的数据库路径
DATABASE_URL = settings.DATABASE_URL

# SQLite 需要额外参数避免线程冲突
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 创建 SessionLocal，每个请求都会使用
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建 ORM 基类
Base = declarative_base()
