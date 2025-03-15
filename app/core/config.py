from pydantic_settings import BaseSettings  # 从 pydantic-settings 导入

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"  # 读取 .env 配置

settings = Settings()
