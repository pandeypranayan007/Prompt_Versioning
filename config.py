from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/promptdeck"
    REDIS_URL: str = "redis://localhost:6379/0"
    JWT_SECRET: str = "super-secret-dev-key"

    class Config:
        env_file = ".env"

settings = Settings()