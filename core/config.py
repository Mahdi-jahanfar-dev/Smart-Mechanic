from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    JWT_SECRET_KEY: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_PORTS: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
